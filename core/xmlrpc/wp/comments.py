from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django_xmlrpc.decorators import xmlrpc_func
from zinnia.models import Category
from zinnia.settings import PROTOCOL
from zinnia.xmlrpc import metaweblog

### Comments
### Just a shim
## <https://codex.wordpress.org/XML-RPC_WordPress_API/Categories_%26_Tags>


@xmlrpc_func(returns='struct[]', args=['integer', 'string', 'string', 'string'])
def get_comment_count(blog_id, username, password, post_id):
    """wp.getCommentCount(blog_id, username, password, post_id)
    => comment structure[]"""
    return [
        {
            'approved': 0,
            'awaiting_moderation': 0,
            'spam': 0,
            'total_comments': 0,
        },
    ]

@xmlrpc_func(returns='struct', args=['integer', 'string', 'string', 'integer'])
def get_comment(blog_id, username, password, comment_id):
    """wp.getCommentCount(blog_id, username, password, comment_id)
    => comment structure"""
    return None

@xmlrpc_func(returns='struct[]', args=['integer', 'string', 'string', 'struct'])
def get_comments(blog_id, username, password, filter):
    """wp.getComments(blog_id, username, password, filter)
    => comment structure[]"""
    return []

@xmlrpc_func(returns='integer', args=['integer', 'string', 'string', 'integer', 'struct'])
def new_comment(blog_id, username, password, post_id, comment):
    """wp.newComment(blog_id, username, password, post_id, comment)
    => comment integer"""
    return -1

@xmlrpc_func(returns='boolean', args=['integer', 'string', 'string', 'integer', 'struct'])
def edit_comment(blog_id, username, password, comment_id, comment):
    """wp.editComment(blog_id, username, password, comment_id, comment)
    => comment boolean"""
    return True

@xmlrpc_func(returns='boolean', args=['integer', 'string', 'string', 'integer'])
def delete_comment(blog_id, username, password, post_id, comment_id):
    """wp.deleteComment(blog_id, username, password, comment_id)
    => comment boolean"""
    return True

@xmlrpc_func(returns='struct[]', args=['integer', 'string', 'string'])
def get_comment_status_list(blog_id, username, password):
    """wp.getCommentStatusList(blog_id, username, password)
    => comment structure[]"""
    return []
