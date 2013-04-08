from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django_xmlrpc.decorators import xmlrpc_func
from tagging.models import Tag
from zinnia.settings import PROTOCOL

### Tags
### Deprecated for WordPress, but useful for us
## <https://codex.wordpress.org/XML-RPC_WordPress_API/Categories_%26_Tags>

def wp_tag_structure(tag, site):
    """A category structure"""
    return {'tag_id': tag.pk,
            'name': tag.name,
            'slug': slugify(tag.name),
            'count': tag.items.count(),
            'html_url': '{0}://{1}{2}'.format(
                PROTOCOL, site.domain,
                reverse('zinnia_tag_detail', args=[tag.name])),
            'rss_url': '{0}://{1}{2}'.format(
                PROTOCOL, site.domain,
                reverse('zinnia_tag_feed', args=[category.tree_path])),
}

@xmlrpc_func(returns='struct[]', args=['integer', 'string', 'string'])
def get_tags(blog_id, username, password):
    """wp.getTags(blog_id, username, password)
    => tag structure[]"""
    authenticate(username, password)
    site = Site.objects.get_current()
    return [wp_tag_structure(tag, site) \
            for tag in Tag.objects.all()]
