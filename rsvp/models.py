from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from rsvp.utils import create_token

class Person(models.Model):
    """ Represent an invitee """
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=254, blank=True, unique=True)
    is_attending = models.BooleanField()
    is_on_inner_envelope = models.BooleanField(default=True)

    def __unicode__(self):
        if self.email:
            return u'{0} <{1}>'.format(self.name, self.email)
        else:
            return u'{0}'.format(self.name)

class Party(models.Model):
    """ Represent a party """

    NEITHER = 'N'
    BRIDE = 'B'
    GROOM = 'G'
    MUTUAL = 'M'
    ALIGNMENT_CHOICES = (
        (NEITHER, 'None'),
        (BRIDE, 'Bride'),
        (GROOM, 'Groom'),
        (MUTUAL, 'Mutual'),
    )

    name = models.CharField(max_length=100, blank=False)
    members = models.ManyToManyField(Person, blank=True, null=True, help_text='Members of a party.')
    token = models.CharField(max_length=64, blank=False, editable=False, default=create_token)
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True, verbose_name='Last updated')
    is_invited = models.BooleanField(verbose_name='Was invited?')
    is_confirmed = models.BooleanField(verbose_name='Has confirmed?')
    alignment = models.CharField(max_length=1, choices=ALIGNMENT_CHOICES, default=NEITHER)

    class Meta:
        verbose_name_plural = 'parties'

    def get_absolute_url(self):
        return reverse('respondez', args=[self.token])

    @property
    def has_rsvped(self):
       """ Return a headcount for the party """
       return self.members.filter(is_attending=True).count()

    @property
    def attending(self):
       """ Return a headcount for the party """
       return self.members.filter(is_attending=True).count()

    @property
    def invitees(self):
        """ Return a theoretical headcount for the party """
        return self.members.count()

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

