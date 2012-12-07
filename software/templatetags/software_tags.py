from django import template
from tagging.models import Tag
from software.models import Software

register = template.Library()

## Show tag links for all tags
#@register.inclusion_tag('software/tag_links_snippet.html', takes_context=True)
#def render_tag_links(context):
#    return {
#        'tags': Tag.objects.usage_for_model(Software)
#    }

# Show tag lnks in the lead of detail pages
@register.inclusion_tag('software/tag_links_detail_snippet.html', takes_context=True)
def render_tag_links_detail(context, obj):
    return {
        'tags': Tag.objects.get_for_object(obj)
    }
