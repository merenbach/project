from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView

urlpatterns = patterns('',
        (r'^$', 'contact.views.send_message'),
        (r'^thanks/$', 'contact.views.thanks'),
        )
