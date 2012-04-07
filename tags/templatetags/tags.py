from django import template
#from django.contrib.auth import models as auth_models

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
