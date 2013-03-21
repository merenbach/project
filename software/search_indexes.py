from django.utils import timezone
from django.conf import settings
from haystack import indexes
from software.models import Software

class SoftwareIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    #title = indexes.CharField(model_attr='title')
    url = indexes.CharField(model_attr='get_absolute_url')
    #title = CharField(model_attr='title')
    #description = CharField(model_attr='description')
    #author = CharField(model_attr='user')
    pub_date = indexes.DateTimeField(model_attr='pub_date')
    pub_site = indexes.IntegerField(model_attr='site__id')
    is_published = indexes.BooleanField(model_attr='is_published')

    def prepare_pub_site(self, obj):
        return obj.site.id

    def get_model(self):
        return Software

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=timezone.now()).filter(is_published=True)
