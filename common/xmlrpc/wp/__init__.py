# Replacement for Zinnia XMLRPC methods
# Maybe someone else might be interested in these someday...
WP_ZINNIA_XMLRPC_METHODS = [
    # Pages (all shims)
    ('common.xmlrpc.wp.pages.get_page',
     'wp.getPage'),
    ('common.xmlrpc.wp.pages.get_pages',
     'wp.getPages'),
    ('common.xmlrpc.wp.pages.get_page_list',
     'wp.getPageList'),
    ('common.xmlrpc.wp.pages.new_page',
     'wp.newPage'),
    ('common.xmlrpc.wp.pages.edit_page',
     'wp.editPage'),
    ('common.xmlrpc.wp.pages.delete_page',
     'wp.deletePage'),
    ('common.xmlrpc.wp.pages.get_page_status_list',
     'wp.getPageStatusList'),
    ('common.xmlrpc.wp.pages.get_page_templates',
     'wp.getPageTemplates'),
    # Posts
    ('common.xmlrpc.wp.posts.get_post',
     'wp.getPost'),
    ('common.xmlrpc.wp.posts.get_posts',
     'wp.getPosts'),
    ('common.xmlrpc.wp.posts.new_post',
     'wp.newPost'),
    ('common.xmlrpc.wp.posts.edit_post',
     'wp.editPost'),
    ('common.xmlrpc.wp.posts.get_post_type',
     'wp.getPostType'), # shim
    ('common.xmlrpc.wp.posts.get_post_types',
     'wp.getPostTypes'), # shim
    ('common.xmlrpc.wp.posts.get_post_formats',
     'wp.getPostFormats'), # shim
    ('common.xmlrpc.wp.posts.get_post_status_list',
     'wp.getPostStatusList'),
    # Categories
    ('common.xmlrpc.wp.categories.get_categories',
     'wp.getCategories'),
    ('common.xmlrpc.wp.categories.suggest_categories',
     'wp.suggestCategories'),
    ('common.xmlrpc.wp.categories.new_category',
     'wp.newCategory'),
    ('common.xmlrpc.wp.categories.delete_category',
     'wp.deleteCategory'),
    # Tags
    ('common.xmlrpc.wp.tags.get_tags',
     'wp.getTags'),
]
