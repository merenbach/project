"""XML-RPC methods of Zinnia metaWeblog API"""
import os
from datetime import datetime
from xmlrpclib import Fault
from xmlrpclib import DateTime

from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.utils.translation import gettext as _
from django.utils.text import Truncator
from django.utils.html import strip_tags
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.template.defaultfilters import slugify

from zinnia.models import Entry
from zinnia.models import Category
from zinnia.settings import PROTOCOL
from zinnia.settings import UPLOAD_TO
from zinnia.managers import DRAFT, PUBLISHED
from django_xmlrpc.decorators import xmlrpc_func

from zinnia.xmlrpc import metaweblog

## TODO
#
# - Can we make wp.addCategory work with MovableType?
# - Would text filters make our Markdown more flexible?

# [am] 
import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
# # [/am]

def localize_date(dt):
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
            post['dateCreated'].value,
            ignoretz=True
        )
        if settings.USE_TZ:
            creation_date = timezone.make_aware(
                creation_date, timezone.utc)
        return DateTime(creation_date.isoformat())
    except:
        return dt

# Some slight modifications
def post_structure(entry, site):
    """A post structure with extensions"""
    s = metaweblog.post_structure(entry, site)
    
    # Replace HTML description with the raw goods (TM)
    # Support Markdown: Burn a Rich Text Editor today!
    if 'description' in s:
        s['description'] = unicode(entry.content)
        
    # Add a markdown slug
    if 'wp_slug' in s:
        s['mt_basename'] = s['wp_slug']
    
    # Use mt_tags instead of mt_keywords
    if 'mt_keywords' in s:
        s['mt_tags'] = s['mt_keywords']
    creation_date = timezone.make_naive(entry.creation_date, timezone.get_default_timezone()).isoformat()
    s.update({
        # [am] Custom extension
        'post_status': entry.get_status_display(),
        'dateCreated': DateTime(creation_date),
    })
    return s

# Copied nearly verbatim from metaweblog.py
@xmlrpc_func(returns='struct', args=['string', 'string', 'string'])
def get_post(post_id, username, password):
    """metaWeblog.getPost(post_id, username, password)
    => post structure"""
    logger.error("GETPOST")
    user = metaweblog.authenticate(username, password)
    site = Site.objects.get_current()
    return post_structure(Entry.objects.get(id=post_id, authors=user), site)

# Copied nearly verbatim from metaweblog.py
@xmlrpc_func(returns='struct[]',
             args=['string', 'string', 'string', 'integer'])
def get_recent_posts(blog_id, username, password, number):
    """metaWeblog.getRecentPosts(blog_id, username, password, number)
    => post structure[]"""
    logger.error("GETRECENTPOSTS")
    user = metaweblog.authenticate(username, password)
    site = Site.objects.get_current()
    return [post_structure(entry, site) \
            for entry in Entry.objects.filter(authors=user)[:number]]

# Modified for MovableType
@xmlrpc_func(returns='string', args=['string', 'string', 'string',
                                     'struct', 'boolean'])
def new_post(blog_id, username, password, post, publish):
    """metaWeblog.newPost(blog_id, username, password, post, publish)
    => post_id"""
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
        post['dateCreated'] = localize_date(post['dateCreated'])
    return metaweblog.new_post(blog_id, username, password, post, publish)

# [am] custom, in-progress
@xmlrpc_func(returns='struct[]', args=['string', 'string', 'string'])
def get_post_categories(post_id, username, password):
    """mt.getPostCategories(post_id, username, password)
    => struct[]"""
    logger.error("GET CATEGORIES")
    user = metaweblog.authenticate(username, password)
    entry = Entry.objects.get(id=post_id, authors=user)
    return [cat.title for cat in entry.categories.all()]
    
# [am] custom, in-progress
@xmlrpc_func(returns='boolean', args=['string', 'string', 'string', 'struct[]'])
def set_post_categories(post_id, username, password, categories):
    """mt.setPostCategories(post_id, username, password, categories)
    => boolean"""
    logger.error("SET CATEGORIES: " + categories)
    user = metaweblog.authenticate(username, password)
    entry = Entry.objects.get(id=post_id, authors=user)
    try:
        entry.categories.clear()
        entry.categories.add(*[Category.objects.get_or_create(
            title=cat['categoryName'], slug=slugify(cat['categoryName']))[0]
                           for cat in categories])
        return True
    except Exception as e:
        return False

# Custom extension for MovableType
@xmlrpc_func(returns='boolean', args=['string', 'string', 'string',
                                      'struct', 'boolean'])
def edit_post(post_id, username, password, post, publish):
    """metaWeblog.editPost(post_id, username, password, post, publish)
    => boolean"""
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
        post['dateCreated'] = localize_date(post['dateCreated'])
    return metaweblog.edit_post(post_id, username, password, post, publish)
