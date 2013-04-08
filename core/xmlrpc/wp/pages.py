from django_xmlrpc.decorators import xmlrpc_func

### Needed as a shim for some clients to support WordPress.
### https://codex.wordpress.org/XML-RPC_WordPress_API/Pages

# Retrieve a single page.
@xmlrpc_func(returns='struct',
             args=['integer', 'integer', 'string', 'string'])
def get_page(blog_id, page_id, username, password):
    """wp.getPage(blog_id, page_id, username, password)
    => page structure"""
    return {}

# Retrieve a complete list of all pages and their details.
@xmlrpc_func(returns='struct[]',
             args=['integer', 'string', 'string', 'integer'])
def get_pages(blog_id, username, password, max_pages=10):
    """wp.getPages(blog_id, username, password, max_pages=10)
    => page structure[]"""
    return []

# Retrieve a complete list of all pages and basic details.
@xmlrpc_func(returns='struct[]',
             args=['integer', 'string', 'string'])
def get_page_list(blog_id, username, password):
    """wp.getPages(blog_id, username, password)
    => page structure[]"""
    return []

# Create a page.
@xmlrpc_func(returns='integer',
             args=['integer', 'string', 'string', 'struct', 'boolean'])
def new_page(blog_id, username, password, content, publish):
    """wp.newPage(blog_id, username, password, content, publish)
    => integer page_id"""
    return -1

# Edit a page.
@xmlrpc_func(returns='boolean',
             args=['integer', 'integer', 'string', 'string', 'struct', 'boolean'])
def edit_page(blog_id, page_id, username, password, content, publish):
    """wp.editPage(blog_id, page_id, username, password, content, publish)
    => boolean"""
    return True

# Delete a page.
@xmlrpc_func(returns='boolean',
             args=['integer', 'string', 'string', 'integer'])
def delete_page(blog_id, username, password, page_id):
    """wp.deletePage(blog_id, username, password, page_id)
    => boolean"""
    return True

# Get page status list.
@xmlrpc_func(returns='struct',
             args=['integer', 'string', 'string'])
def get_page_status_list(blog_id, username, password):
    """wp.getPageStatusList(blog_id, username, password)
    => page structure"""
    return {}

# Get page status list.
@xmlrpc_func(returns='struct',
             args=['integer', 'string', 'string'])
def get_page_templates(blog_id, username, password):
    """wp.getPageTemplates(blog_id, username, password)
    => page structure"""
    return {}

