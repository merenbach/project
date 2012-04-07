#import datetime
from haystack import indexes
from django.contrib.flatpages.models import FlatPage

class FlatPageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    #text = models.CharField(model_attr='content')
    title = indexes.CharField(model_attr='title')
    url = indexes.CharField(model_attr='url')

    def get_model(self):
        return FlatPage

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
