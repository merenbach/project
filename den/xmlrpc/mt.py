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

# [TODO]
#
# - Simply extend existing metaweblog API and rebrand as "mt.py"
# - Make adding *entirely new* categories work
# - Markdown text filter?

# [am] 
import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
# # [/am]

# Some slight modifications
def post_structure(entry, site):
    """A post structure with extensions"""
    s = metaweblog.post_structure(entry, site)
    s.update({
        # [am] Custom extension
        'description': unicode(entry.content),
        'post_status': entry.get_status_display(),
        'mt_basename': entry.slug,
        'mt_tags': entry.tags,
        #'mt_keywords': entry.tags,
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
    # user = metaweblog.authenticate(username, password, 'zinnia.add_entry')
    # if post.get('dateCreated'):
    #     creation_date = datetime.strptime(
    #         post['dateCreated'].value[:18], '%Y-%m-%dT%H:%M:%S')
    #     if settings.USE_TZ:
    #         creation_date = timezone.make_aware(
    #             creation_date, timezone.utc)
    # else:
    #     creation_date = timezone.now()
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
    # if post.get('dateCreated'):
    #     creation_date = datetime.strptime(
    #         post['dateCreated'].value[:18], '%Y-%m-%dT%H:%M:%S')
    #     if settings.USE_TZ:
    #         creation_date = timezone.make_aware(
    #             creation_date, timezone.utc)
    return metaweblog.edit_post(post_id, username, password, post, publish)
