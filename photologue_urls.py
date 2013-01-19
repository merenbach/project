from django.conf.urls import *
from photologue.views import PhotoListView, PhotoDetailView, GalleryListView, \
    GalleryDetailView, PhotoArchiveIndexView, PhotoDateDetailView, PhotoDayArchiveView, \
    PhotoYearArchiveView, PhotoMonthArchiveView, GalleryArchiveIndexView, GalleryYearArchiveView, \
    GalleryDateDetailView, GalleryDayArchiveView, GalleryMonthArchiveView


urlpatterns = patterns('',

    # url(r'^gallery/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[\-\d\w]+)/$',
    #         GalleryDateDetailView.as_view(month_format='%m', day_format='%d'),
    #         name='pl-gallery-detail'),
    #     url(r'^gallery/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',
    #         GalleryDayArchiveView.as_view(month_format='%m', day_format='%d'),
    #         name='pl-gallery-archive-day'),
    #     url(r'^gallery/(?P<year>\d{4})/(?P<month>\d{2})/$',
    #         GalleryMonthArchiveView.as_view(month_format='%m'),
    #         name='pl-gallery-archive-month'),
    #     url(r'^gallery/(?P<year>\d{4})/$',
    #         GalleryYearArchiveView.as_view(),
    #         name='pl-gallery-archive-year'),
    url(r'^gallery/$', 
        GalleryArchiveIndexView.as_view(allow_empty=True),
        name='pl-gallery-archive'),
                        
    url(r'^gallery/(?P<slug>[\-\d\w]+)/$', GalleryDetailView.as_view() , name='pl-gallery'),
    url(r'^gallery/page/(?P<page>[0-9]+)/$', GalleryListView.as_view(allow_empty=True), name='pl-gallery-list'),

    # url(r'^photo/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[\-\d\w]+)/$',
    #        PhotoDateDetailView.as_view(month_format='%m', day_format='%d'),
    #        name='pl-photo-detail'),
    #    url(r'^photo/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',
    #        PhotoDayArchiveView.as_view(month_format='%m', day_format='%d'),
    #        name='pl-photo-archive-day'),
    #    url(r'^photo/(?P<year>\d{4})/(?P<month>\d{2})/$',
    #        PhotoMonthArchiveView.as_view(month_format='%m'),
    #        name='pl-photo-archive-month'),
    #    url(r'^photo/(?P<year>\d{4})/$',
    #        PhotoYearArchiveView.as_view(),
    #        name='pl-photo-archive-year'),
    url(r'^photo/$', 
        PhotoArchiveIndexView.as_view(allow_empty=True),
        name='pl-photo-archive'),

    url(r'^photo/(?P<slug>[\-\d\w]+)/$',
        PhotoDetailView.as_view(),
        name='pl-photo'),
    url(r'^photo/page/(?P<page>[0-9]+)/$',
        PhotoListView.as_view(allow_empty=True),
        name='pl-photo-list'),

)


