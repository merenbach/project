# Replacement for Zinnia XMLRPC methods
# Maybe someone else might be interested in these someday...
WP_ZINNIA_XMLRPC_METHODS = [
    # Pages (all shims)
    ('core.xmlrpc.wp.pages.get_page',
     'wp.getPage'),
    ('core.xmlrpc.wp.pages.get_pages',
     'wp.getPages'),
    ('core.xmlrpc.wp.pages.get_page_list',
     'wp.getPageList'),
    ('core.xmlrpc.wp.pages.new_page',
     'wp.newPage'),
    ('core.xmlrpc.wp.pages.edit_page',
     'wp.editPage'),
    ('core.xmlrpc.wp.pages.delete_page',
     'wp.deletePage'),
    ('core.xmlrpc.wp.pages.get_page_status_list',
     'wp.getPageStatusList'),
    ('core.xmlrpc.wp.pages.get_page_templates',
     'wp.getPageTemplates'),
    # Posts
    ('core.xmlrpc.wp.posts.get_post',
     'wp.getPost'),
    ('core.xmlrpc.wp.posts.get_posts',
     'wp.getPosts'),
    ('core.xmlrpc.wp.posts.new_post',
     'wp.newPost'),
    ('core.xmlrpc.wp.posts.edit_post',
     'wp.editPost'),
    ('core.xmlrpc.wp.posts.get_post_type',
     'wp.getPostType'), # shim
    ('core.xmlrpc.wp.posts.get_post_types',
     'wp.getPostTypes'), # shim
    ('core.xmlrpc.wp.posts.get_post_formats',
     'wp.getPostFormats'), # shim
    ('core.xmlrpc.wp.posts.get_post_status_list',
     'wp.getPostStatusList'),
    # Categories
    ('core.xmlrpc.wp.categories.get_categories',
     'wp.getCategories'),
    ('core.xmlrpc.wp.categories.suggest_categories',
     'wp.suggestCategories'),
    ('core.xmlrpc.wp.categories.new_category',
     'wp.newCategory'),
    ('core.xmlrpc.wp.categories.delete_category',
     'wp.deleteCategory'),
    # Tags
    ('core.xmlrpc.wp.tags.get_tags',
     'wp.getTags'),
]
