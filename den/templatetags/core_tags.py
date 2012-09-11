from django import template
from django.core.urlresolvers import reverse
# from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag(takes_context=True)
def active(context, pattern):
    request = context.get('request', None)
    if request is not None:
        import re
        pattern = u'^{}$'.format(pattern)
        if re.search(pattern, request.path):
            return 'active'
    return ''

@register.simple_tag(takes_context=True)
def make_crumbs(context, *args, **kwargs):
    """ Make a first-level breadcrumb trail with the given title. """
    request = context.get('request', None)
    if request is not None and len(args) > 0:
        if len(args) == 1:
            request.breadcrumbs(args[0], request.path_info)
        elif len(args) == 2:
            title = args[0]
            url = args[1]
            request.breadcrumbs(title, url)
        elif len(args) > 2:
            title = args[0]
            url = args[1]
            request.breadcrumbs(title, reverse(url, args=args[2:], kwargs=kwargs))
        # request.breadcrumbs(mark_safe(''.join(args)), request.path_info)
    return ''

# [am] added this on 2011-11-05
#@register.inclusion_tag('cmsplugin_blog/tag_links_detail_snippet.html', takes_context=True)
#def render_tag_links_detail(context, obj):
#    request = context["request"]
#    language = get_language_from_request(request)
#    kw = get_translation_filter_language(Entry, language)
#    filters = dict(is_published=True, pub_date__lte=datetime.datetime.now(), **kw)
#    return {
#        'tags': Tag.objects.get_for_object(obj)
#    }
