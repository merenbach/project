from django import template
from django.core.urlresolvers import reverse
# from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag(takes_context=True)
def active(context, pattern):
    """ Try to determine whether a link is active """
    request = context.get('request', None)
    if request is not None:
        if pattern == request.path:
            return u'active'
        elif pattern != '/':
            import re
            # Use "match" instead of "search" to find from beginning
            if re.match(pattern, request.path):
                return u'active'
    return u''

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

@register.filter(name='is_checkbox')
def is_checkbox(field):
    """ From http://stackoverflow.com/questions/3927018/django-how-to-check-if-field-widget-is-checkbox-in-the-template """
    from django.forms import CheckboxInput
    return field.field.widget.__class__.__name__ == CheckboxInput().__class__.__name__
