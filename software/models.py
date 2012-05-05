import os
from django.db import models
from django.db.models import permalink
from django.template.defaultfilters import slugify
import datetime
from django.conf import settings

from urlparse import urljoin

from tagging.fields import TagField
from tagging.models import Tag

from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager

SOFTWARE_PATH = os.path.join(settings.STATIC_ROOT, 'software')

#SOFTWARE_CATEGORY_DICT = {
#        'A': 'Application',
#        'P': 'Port',
#        'L': 'Legacy',
#        }
#SOFTWARE_CATEGORY_CHOICES = (
#        ('A', SOFTWARE_CATEGORY_DICT['A']),
#        ('P', SOFTWARE_CATEGORY_DICT['P']),
#        ('L', SOFTWARE_CATEGORY_DICT['L']),
#        )

# Create your models here.
class Software(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50)
    version = models.CharField(max_length=20)
    summary = models.CharField(max_length=200)
    tags = TagField()
    description = models.TextField()
    #category = models.CharField(max_length=1, choices=SOFTWARE_CATEGORY_CHOICES)
    #app_file = models.FileField('app download', upload_to='files/software', blank=True)
    #src_file = models.FileField('source download', upload_to='files/software', blank=True)
    app_file = models.FilePathField('app download', path=SOFTWARE_PATH, blank=True)
    src_file = models.FilePathField('source download', path=SOFTWARE_PATH, blank=True)
    #app_icon = models.ImageField('application icon', upload_to='images/software', blank=True)
    pub_date = models.DateTimeField('date published', blank=True)
    is_published = models.BooleanField('is published')
    site = models.ForeignKey(Site)
    objects = models.Manager()
    on_site = CurrentSiteManager()

    class Meta:
        verbose_name = 'software'
        verbose_name_plural = 'software'
    def __unicode__(self):
        return self.title
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
    was_published_today.short_description = 'Published today?'
    #def published(self):
    #    return self.is_published
    #is_currently_published.short_description = 'Published?'
    def get_tags(self):
        return Tag.objects.get_for_object(self)
    #def get_category_long_name(self):
    #    return SOFTWARE_CATEGORY_DICT[self.category]

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.pub_date:
            self.pub_date = datetime.datetime.today()
        super(Software, self).save(*args, **kwargs)

    def get_file_url(self, filepath):
        relpath = os.path.relpath(filepath, settings.MEDIA_ROOT)
        return urljoin(settings.MEDIA_URL, relpath)
    def get_file_size(self, filepath):
        return os.path.getsize(filepath)

    def get_app_file_url(self):
        return self.get_file_url(self.app_file)
    def get_app_file_size(self):
        return self.get_file_size(self.app_file)

    def get_src_file_url(self):
        return self.get_file_url(self.src_file)
    def get_src_file_size(self):
        return self.get_file_size(self.src_file)

    @permalink
    def get_absolute_url(self):
        return ('software_detail', None, { 'slug': self.slug })

