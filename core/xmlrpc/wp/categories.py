from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django_xmlrpc.decorators import xmlrpc_func
from zinnia.models import Category
from zinnia.settings import PROTOCOL
from zinnia.xmlrpc import metaweblog

### Categories
### Deprecated for WordPress, but useful for us
## <https://codex.wordpress.org/XML-RPC_WordPress_API/Categories_%26_Tags>

def wp_category_suggestion(category):
    return {
        'categoryId': category.pk,
        'categoryName': category.title,
    }

@xmlrpc_func(returns='struct[]', args=['integer', 'string', 'string'])
def get_categories(blog_id, username, password):
    """wp.getCategories(blog_id, username, password)
    => category structure[]"""
    return metaweblog.get_categories(blog_id, username, password)

@xmlrpc_func(returns='struct[]', args=['integer', 'string', 'string', 'string', 'integer'])
def suggest_categories(blog_id, username, password, category_name, max_results):
    """wp.suggestCategories(blog_id, username, password, category, max_results)
    => category structure[]"""
    return [wp_category_suggestion(category) \
            for category in Category.objects.all() \
            if category.startswith(category_name)][:max_results]

# Override existing new_category to properly account for possible missing data
@xmlrpc_func(returns='integer', args=['integer', 'string', 'string', 'struct'])
def new_category(blog_id, username, password, category_struct):
    """wp.newCategory(blog_id, username, password, category)
    => category structure[]"""
    category_struct.setdefault('description', '')
    category_struct.setdefault('slug', slugify(category_struct['name']))
    category_struct.setdefault('parent_id', 0)
    return metaweblog.new_category(blog_id, username, password, category_struct)

@xmlrpc_func(returns='boolean', args=['integer', 'string', 'string', 'integer'])
def delete_category(blog_id, username, password, category_id):
    """wp.deleteCategory(blog_id, username, password, category)
    => boolean"""
    Category.objects.get(pk=category_id).delete()
    return True
