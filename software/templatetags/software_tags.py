import datetime
from django import template
from django.contrib.auth import models as auth_models

from tagging.models import Tag

from software.models import Software

register = template.Library()

@register.inclusion_tag('software/tag_links_snippet.html', takes_context=True)
def render_tag_links(context):
    #request = context["request"]
    #language = get_language_from_request(request)
    #kw = get_translation_filter_language(Software, language)
    #filters = dict(is_published=True, pub_date__lte=datetime.datetime.now(), **kw)
    return {
        'tags': Tag.objects.usage_for_model(Software)
    }

# [am] added this on 2011-11-05
@register.inclusion_tag('software/tag_links_detail_snippet.html', takes_context=True)
def render_tag_links_detail(context, obj):
    #request = context["request"]
    #language = get_language_from_request(request)
    #kw = get_translation_filter_language(Entry, language)
    #filters = dict(is_published=True, pub_date__lte=datetime.datetime.now(), **kw)
    return {
        'tags': Tag.objects.get_for_object(obj)
        #'tags': Tag.objects.usage_for_model(Entry, filters=filters)
    }

