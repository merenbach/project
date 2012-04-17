import datetime
from project import settings
from haystack import indexes
from project.websites.merenbach.software.models import Software

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
    #def get_queryset(self):
    #    return Software.objects.filter(is_published=True, pub_date__lte=datetime.datetime.now())

    def prepare_pub_site(self, obj):
        return obj.site.id

    def get_model(self):
        return Software

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now()).filter(is_published=True)
