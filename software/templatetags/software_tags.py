from django import template
from django.template.defaultfilters import stringfilter

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

@register.filter
@stringfilter
def swfile(value):
    """ Return True if we can acquire a lock on a file, False otherwise """
    try:
        with open(value) as f:
            return True;
    except IOError as e:
        return False

@register.filter
@stringfilter
def swlink(value):
    """ Return the download link for a file """
    from os.path import relpath
    from urlparse import urljoin
    from django.conf import settings
    return urljoin(settings.MEDIA_URL, relpath(value, settings.MEDIA_ROOT))

@register.filter
@stringfilter
def swsize(value):
    """ Return the size of a download """
    from os.path import getsize
    try:
        with open(value) as f:
            return getsize(value)
    except IOError as e:
        return (-1)
