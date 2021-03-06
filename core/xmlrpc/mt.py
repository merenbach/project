"""XML-RPC methods of Zinnia metaWeblog API"""
from xmlrpclib import DateTime

from django.conf import settings
from django.utils import timezone
from django.contrib.sites.models import Site
from django.utils.translation import gettext as _
from django.template.defaultfilters import slugify

from zinnia.models import Entry
from zinnia.models import Category
from zinnia.managers import DRAFT, HIDDEN, PUBLISHED
from django_xmlrpc.decorators import xmlrpc_func

from zinnia.xmlrpc import metaweblog

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)

## TODO
#
# - Can we make wp.addCategory work with MovableType?
# - Would text filters make our Markdown more flexible?
# - Make exception checks more exception-specific (?)
# - Ensure logging is as optimized as it ought to be
# - Translate additional post statuses properly
# - Add more WordPress methods

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
    # This is not currently supported in Zinnia (2013-04-08)
    # if 'post_status' in post and post['post_status'] == u'private':
    #     post['post_status'] = u'hidden'
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
    if entry.login_required:
        # This could be 'protected' if our client supports it in the future
        s['post_status'] = u'private'
    elif entry.status == HIDDEN:
        s['post_status'] = u'pending'
    else:
        s['post_status'] = entry.get_status_display()
    return s

# Copied nearly verbatim from metaweblog.py
@xmlrpc_func(returns='struct', args=['string', 'string', 'string'])
def get_post(post_id, username, password):
    """metaWeblog.getPost(post_id, username, password)
    => post structure"""
    user = metaweblog.authenticate(username, password)
    site = Site.objects.get_current()
    return post_structure(Entry.objects.get(id=post_id, authors=user), site)

# Copied nearly verbatim from metaweblog.py
@xmlrpc_func(returns='struct[]',
             args=['string', 'string', 'string', 'integer'])
def get_recent_posts(blog_id, username, password, number):
    """metaWeblog.getRecentPosts(blog_id, username, password, number)
    => post structure[]"""
    user = metaweblog.authenticate(username, password)
    site = Site.objects.get_current()
    return [post_structure(entry, site) \
            for entry in Entry.objects.filter(authors=user, sites__id=blog_id)[:number]]

# Internal method to align with WordPress
def update_post_status(post_id, username, password, post):
    # Update status as appropriate
    if u'post_status' in post:
        user = metaweblog.authenticate(username, password, 'zinnia.change_entry')
        entry = Entry.objects.get(id=post_id, authors=user)
        post_status = post.get('post_status')
        if post_status == u'private':
            entry.login_required = True
            entry.status = PUBLISHED
        else:
            entry.login_required = False
            if post_status == u'draft':
                entry.status = DRAFT
            elif post_status == u'pending':
                entry.status = HIDDEN
            else:
                entry.status = PUBLISHED
        entry.save()

# Modified for MovableType
@xmlrpc_func(returns='string', args=['string', 'string', 'string',
                                     'struct', 'boolean'])
def new_post(blog_id, username, password, post, publish):
    """metaWeblog.newPost(blog_id, username, password, post, publish)
    => post_id"""
    post_id = metaweblog.new_post(blog_id, username, password, finesse_fields_to_commit(post), publish)
    update_post_status(post_id, username, password, post)
    return post_id

# Custom extension for MovableType
@xmlrpc_func(returns='boolean', args=['string', 'string', 'string',
                                      'struct', 'boolean'])
def edit_post(post_id, username, password, post, publish):
    """metaWeblog.editPost(post_id, username, password, post, publish)
    => boolean"""
    success = metaweblog.edit_post(post_id, username, password, finesse_fields_to_commit(post), publish)
    update_post_status(post_id, username, password, post)
    return success

# Get categories
@xmlrpc_func(returns='struct[]', args=['string', 'string', 'string'])
def get_post_categories(post_id, username, password):
    """mt.getPostCategories(post_id, username, password)
    => struct[]"""
    user = metaweblog.authenticate(username, password)
    site = Site.objects.get_current()
    entry = Entry.objects.get(id=post_id, authors=user)
    return [metaweblog.category_structure(category, site) \
        for category in entry.categories.all()]
    
# Set categories
@xmlrpc_func(returns='boolean', args=['string', 'string', 'string', 'struct[]'])
def set_post_categories(post_id, username, password, categories):
    """mt.setPostCategories(post_id, username, password, categories)
    => boolean"""
    user = metaweblog.authenticate(username, password)
    entry = Entry.objects.get(id=post_id, authors=user)
    try:
        entry.categories.clear()
        entry.categories.add(*[Category.objects.get_or_create(
            title=cat['categoryName'], slug=slugify(cat['categoryName']))[0]
                           for cat in categories])
        return True
    except Exception as e:
        logger.error(e)
        return False
