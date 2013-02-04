from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site
from rsvp.utils import create_token

class Person(models.Model):
    """ Represent an invitee """
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=254, blank=True, unique=True)
    is_attending = models.BooleanField()
    is_on_inner_envelope = models.BooleanField(default=True)

    def __unicode__(self):
        return u'{0} <{1}>'.format(self.name, self.email)

class Party(models.Model):
    """ Represent a party """
    name = models.CharField(max_length=100, blank=False)
    members = models.ManyToManyField(Person, blank=True, null=True, help_text='Members of a party.')
    token = models.CharField(max_length=64, blank=False, editable=False, default=create_token)
    creation_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'parties'

    @property
    def headcount(self):
    	""" Return a headcount for the party """
    	return members.filter_by(is_attending=True).count()

    def __unicode__(self):
        return u'{0}'.format(self.name)

class RSVP(models.Model):
    """ Represent an invitee """
    site = models.ForeignKey(Site, default=Site.objects.get_current)
    party = models.ForeignKey(Party, unique=True)
    message = models.TextField(blank=True, help_text='An optional message for the happy couple.')
    rsvp_date = models.DateField(auto_now=True)

    def __unicode__(self):
        return u'RSVP for {0}'.format(self.party.name)

