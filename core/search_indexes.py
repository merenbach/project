from haystack import indexes
from django.contrib.flatpages.models import FlatPage
#from django.contrib.sites.models import Site
#from core.indexes import SiteSearchIndex

class FlatPageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    url = indexes.CharField(model_attr='url')
    sites = indexes.MultiValueField(model_attr='sites__all')

    def get_model(self):
        return FlatPage

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
