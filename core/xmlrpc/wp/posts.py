"""XML-RPC methods of Zinnia metaWeblog API"""
from xmlrpclib import DateTime

from django.conf import settings
from django.utils import timezone
from django.contrib.sites.models import Site
from django_xmlrpc.decorators import xmlrpc_func

#from zinnia.managers import HIDDEN
from zinnia.models import Entry

from zinnia.xmlrpc import metaweblog

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)

## TODO
#
# - Would text filters make our Markdown more flexible?
# - Make exception checks more exception-specific (?)
# - Ensure logging is as optimized as it ought to be

def make_xmlrpc_datetime_aware(dt):
    """
    Localize (or perhaps "serverize") a date.
    This is needed when settings.USE_TZ is on
    in order for posts to be properly set to
    have the correct creation date.
    
    [TODO]: Is this simply nullifying our use
    of USE_TZ?
    """
    import dateutil.parser
    try:
        creation_date = dateutil.parser.parse(
            dt.value,
            ignoretz=True
        )
        if settings.USE_TZ:
            creation_date = timezone.make_aware(
                creation_date, timezone.utc)
        return DateTime(creation_date.isoformat())
    except Exception as e:
        logger.error(e)
        return dt

def make_xmlrpc_datetime_naive(dt):
    """
    Localize (or perhaps "serverize") a date.
    This is needed when settings.USE_TZ is on
    in order for posts to be properly set to
    have the correct creation date.
    
    [TODO]: Is this simply nullifying our use
    of USE_TZ?
    """
    import dateutil.parser
    try:
        creation_date = dateutil.parser.parse(
            dt.value,
            ignoretz=False
        )
        if settings.USE_TZ:
            creation_date = timezone.make_naive(
                creation_date, timezone.get_default_timezone())
        return DateTime(creation_date.isoformat())
    except Exception as e:
        logger.error(e)
        return dt

def finesse_fields_to_commit(post):
    """
    Massage post structure fields before
    committing them to the database.
    """
    if 'mt_tags' in post:
        # Use the MovableType attribute of choice
        post['mt_keywords'] = post['mt_tags']
    if 'mt_basename' in post:
        # Use the MovableType attribute of choice
        post['wp_slug'] = post['mt_basename']
    if 'mt_allow_comments' in post:
        # Convert to integer type
        post['mt_allow_comments'] = int(post['mt_allow_comments'])
    if 'mt_allow_pings' in post:
        # Convert to integer type
        post['mt_allow_pings'] = int(post['mt_allow_pings'])
    if 'dateCreated' in post:
        # Correct possible date format alignment issues
        post['dateCreated'] = make_xmlrpc_datetime_aware(post['dateCreated'])
    return post

def finesse_fields_to_return(struct):
    """
    Massage post structure fields before
    returning them to an XML-RPC client.
    """
    # Add a markdown slug
    if 'wp_slug' in struct:
        struct['mt_basename'] = struct['wp_slug']
    # Use mt_tags instead of mt_keywords
    if 'mt_keywords' in struct:
        struct['mt_tags'] = struct['mt_keywords']
    # Remove categories (we use the MT API instead)
    # if 'categories' in struct:
    #     del struct['categories']
    # Make the datetime naive for clients.  This may
    # have some undesired ramifications, so the
    # implications of these should be investigated.
    if 'dateCreated' in struct:
        struct['dateCreated'] = make_xmlrpc_datetime_naive(struct['dateCreated'])
    return struct

# Some slight modifications
def post_structure(entry, site):
    """A post structure with extensions"""
    s = finesse_fields_to_return(metaweblog.post_structure(entry, site))
    # Replace HTML description with the raw goods (TM)
    # Support Markdown: Burn a Rich Text Editor today!
    if 'description' in s:
        s['description'] = unicode(entry.content)
    # [todo] How is the post status getting sent back for WordPress?
    if s['wp_password'] or entry.login_required:
        s['post_status'] = u'private'
    #elif entry.status == HIDDEN:
    #    s['post_status'] = u'pending'
    else:
        s['post_status'] = entry.get_status_display()
    return s

# Copied nearly verbatim from metaweblog.py
@xmlrpc_func(returns='struct', args=['integer', 'string', 'string', 'integer', 'string[]'])
def get_post(blog_id, username, password, post_id, fields=[]):
    """wp.getPost(blog_id, username, password, post_id, fields=[])
    => post structure"""
    user = metaweblog.authenticate(username, password)
    site = Site.objects.get_current()
    return post_structure(Entry.objects.get(id=post_id, authors=user), site)


@xmlrpc_func(returns='struct[]',
             args=['integer', 'string', 'string', 'struct'])
def get_posts(blog_id, username, password, filter={}):
    """wp.getPosts(blog_id, username, password, number)
    => post structure[]"""
    user = metaweblog.authenticate(username, password)
    site = Site.objects.get_current()
    return [post_structure(entry, site) \
            for entry in Entry.objects.filter(authors=user, sites__id=blog_id)]

@xmlrpc_func(returns='string', args=['integer', 'string', 'string', 'struct'])
def new_post(blog_id, username, password, content):
    """wp.newPost(blog_id, username, password, content)
    => post_id"""
    return metaweblog.new_post(blog_id, username, password, finesse_fields_to_commit(content), publish)

@xmlrpc_func(returns='boolean', args=['integer', 'string', 'string',
                                      'integer', 'struct'])
def edit_post(blog_id, username, password, post_id, content):
    """wp.editPost(blog_id, username, password, post_id, content)
    => boolean"""
    return metaweblog.edit_post(post_id, username, password, finesse_fields_to_commit(content), publish)

@xmlrpc_func(returns='boolean', args=['integer', 'string',
                                      'string', 'integer'])
def delete_post(blog_id, username, password, post_id):
    """wp.deletePost(blog_id, username, password, post_id)
    => boolean"""
    return metaweblog.delete_post(post_id, username, password)

# Shim
@xmlrpc_func(returns='struct', args=['integer', 'string',
                                      'string', 'string', 'string[]'])
def get_post_type(blog_id, username, password, post_type_name, fields=[]):
    """wp.getPostType(blog_id, username, password, post_type_name, fields=[])
    => struct"""
    return {}

# Shim
@xmlrpc_func(returns='struct', args=['integer', 'string',
                                      'string', 'struct', 'string[]'])
def get_post_types(blog_id, username, password, filter={}, fields=[]):
    """wp.getPostTypes(blog_id, username, password, filter={}, fields=[])
    => struct"""
    return {}

# Shim
@xmlrpc_func(returns='struct', args=['integer', 'string',
                                      'string', 'struct[]'])
def get_post_formats(blog_id, username, password, filter=[]):
    """wp.getPostTypes(blog_id, username, password, filter=[])
    => struct"""
    return {}

@xmlrpc_func(returns='struct', args=['integer', 'string', 'string'])
def get_post_status_list(blog_id, username, password):
    """wp.getPostStatusList(blog_id, username, password)
    => struct"""
    return {
        'draft': 'Draft',
        'hidden': 'Hidden',
        'published': 'Published',
    }
