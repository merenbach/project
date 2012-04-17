from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from software.models import Software
from tagging.views import tagged_object_list

urlpatterns = patterns('',
        #url(r'^(?P<slug>[-a-z]+)/$', 'detail'),
        #(r'^(?P<slug>[-\w]+)/$',
        # below works
        url(r'^$',
            ListView.as_view(
                #queryset=Software.objects.order_by('-pub_date')[:5],
                #context_object_name='latest_software_list',
                queryset=Software.objects.filter(is_published=True).order_by('-pub_date'),
                context_object_name='software_list',
                template_name='software/index.html'),
            name='software',
            ),

        url(r'^(?P<slug>[-a-z0-9]+)/$',
            DetailView.as_view(
                queryset=Software.objects.filter(is_published=True).order_by('-pub_date'),
                template_name='software/detail.html'),
            name='software_detail',
            ),

        #(r'^tags/$', 'software.views.tags'),
        #(r'^tag/(?P<tag>[^/]+)/$', 'software.views.with_tag'),
        url(r'^tagged/(?P<tag>[^/]+)/$', tagged_object_list,
            dict(queryset_or_model=Software.objects.filter(is_published=True).order_by('-pub_date'), allow_empty=True,
                template_object_name='software'),
            name='software_tag_detail',
            ),

        #url(r'^(?P<pk>\d+)/results/$',
        #	DetailView.as_view(
        #		model=Poll,
        #		template_name='polls/results.html'),
        #	name='poll_results'),
        #(r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
        )



#urlpatterns = patterns('polls.views',
#    # Examples:
#    # url(r'^$', 'myproject.views.home', name='home'),
#    # url(r'^myproject/', include('myproject.foo.urls')),
#	(r'^$', 'index'),
#	(r'^(?P<poll_id>\d+)/$', 'detail'),
#	(r'^(?P<poll_id>\d+)/results/$', 'results'),
#	(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
#)
