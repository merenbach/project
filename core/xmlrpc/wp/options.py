from django_xmlrpc.decorators import xmlrpc_func

# Shim
@xmlrpc_func(returns='struct[]', args=['integer', 'string', 'string', 'string[]'])
def get_options(blog_id, username, password, options=[]):
    """wp.getOptions(blog_id, username, password, options)
    => options structure[]"""
    return []

# Shim
@xmlrpc_func(returns='struct[]', args=['integer', 'string', 'string', 'struct[]'])
def set_options(blog_id, username, password, options=[]):
    """wp.setOptions(blog_id, username, password, options=[])
    => options structure[]"""
    return []
