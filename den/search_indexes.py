from haystack import indexes
from django.contrib.flatpages.models import FlatPage
from zinnia.models import Entry
#from articles.models import Article
#from django.conf import settings
#from django.contrib.sites.models import Site
#from den.indexes import SiteSearchIndex

class FlatPageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    url = indexes.CharField(model_attr='url')
    sites = indexes.MultiValueField(model_attr='sites__all')

    def prepare_sites(self, obj):
        return [a.id for a in obj.sites.all()]

    def get_model(self):
        return FlatPage

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

class EntryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    excerpt = indexes.CharField(model_attr='excerpt')
    url = indexes.CharField(model_attr='get_absolute_url')
    pub_date = indexes.DateTimeField(model_attr='creation_date')

    #def prepare_sites(self, obj):
    #    return [a.id for a in obj.sites.all()]

    def get_model(self):
        return Entry

    def index_queryset(self):
        """Used when the entire index for model is updated."""
	from zinnia.managers import PUBLISHED
        return self.get_model().published.all()

#class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
#    text = indexes.CharField(document=True, use_template=True)
#    title = indexes.CharField(model_attr='title')
#    url = indexes.CharField(model_attr='get_absolute_url')
#    sites = indexes.MultiValueField(model_attr='sites__all')
#    pub_date = indexes.DateTimeField(model_attr='publish_date')
#
#    def prepare_sites(self, obj):
#        return [a.id for a in obj.sites.all()]
#
#    def get_model(self):
#        return Article
#
#    def index_queryset(self):
#        """Used when the entire index for model is updated."""
#        return self.get_model().objects.live().all()
#
