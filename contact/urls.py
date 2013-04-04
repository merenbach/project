from django.conf.urls import patterns, url, include
from contact.views import ContactView, ContactThanksView
from honeypot.decorators import check_honeypot

urlpatterns = patterns('',
    url(r'^$', check_honeypot(ContactView.as_view()), name='contact'),
    url(r'^thanks/$', ContactThanksView.as_view(), name='contact-thanks'),
)
