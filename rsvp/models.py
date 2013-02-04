from django.db import models

from django.conf import settings

from tagging.fields import TagField
from tagging.models import Tag

from django.contrib.sites.models import Site

class Person(models.Model):
    """ Represent an invitee """
    name = models.CharField(max_length=100, blank=F0alse)
    email = models.EmailField(max_length=254, blank=True, unique=True)
    is_attending = models.BooleanField()

    def __unicode__(self):
        return u'{0} <{1}>'.format(self.name, self.email)

class Party(models.Model):
    """ Represent a party """
    name = models.CharField(max_length=100, blank=False)
    members = models.ManyToManyField(Person, blank=True, null=True, help_text='Members of a party.')
    
    @property
    def headcount(self):
    	""" Return a headcount for the party """
    	return members.filter_by(is_attending=True).count()

    def __unicode__(self):
        return u'Party {0}'.format(self.name)

class RSVP(models.Model):
    """ Represent an invitee """
    site = models.ForeignKey(Site)
    party = models.ForeignKey(Party, unique=True)
    message = models.TextField(blank=True, help_text='An optional message for the happy couple.')
    rsvp_date = models.DateField(auto_now=True)

    def __unicode__(self):
        return u'RSVP for {0}'.format(self.party.name)

