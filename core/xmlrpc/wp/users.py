from django_xmlrpc.decorators import xmlrpc_func
from zinnia.xmlrpc import metaweblog

@xmlrpc_func(returns='struct[]', args=['string', 'string'])
def get_users_blogs(username, password):
    """wp.getUsersBlogs(username, password)
    => blog structure[]"""
    return metaweblog.get_users_blogs(None, username, password)

@xmlrpc_func(returns='struct[]', args=['integer', 'string', 'string'])
def get_authors(blog_id, username, password):
    """wp.getAuthors(blog_id, username, password)
    => author structure[]"""
    return metaweblog.get_authors(None, username, password)
