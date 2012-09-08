from django.conf.urls import patterns, url, include
from contact.views import ContactView, ContactThanksView

urlpatterns = patterns('',
    url(r'^$', ContactView.as_view(), name='contact'),
    url(r'^thanks/$', ContactThanksView.as_view(), name='contact-thanks'),
)
