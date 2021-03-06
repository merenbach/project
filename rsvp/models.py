from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from rsvp.utils import create_token

class Invitee(models.Model):
    """ Represent an invitee """
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=254, blank=True)
    is_party_leader = models.BooleanField(default=True)
    is_attending = models.BooleanField()

    class Meta:
        ordering = ['name']

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

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'parties'

    name = models.CharField(max_length=100, blank=False)
    members = models.ManyToManyField(Invitee, blank=True, null=True, help_text='Members of a party.')
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True, verbose_name='Last updated')
    is_invited = models.BooleanField(verbose_name='Was invited?')
    is_confirmed = models.BooleanField(verbose_name='Has confirmed?')
    alignment = models.CharField(max_length=1, choices=ALIGNMENT_CHOICES, default=NEITHER)

    @property
    def headcount(self):
        """ Return a headcount for the party.  Followers only attend if at least one leader attends. """
        return self.entourage().count()

    def entourage(self):
        """ Return a query for attending party members. Followers only attend if at least one leader attends. """
        attending = self.members.filter(is_attending=True)
        leaders_attending = attending.filter(is_party_leader=True).count()
        if leaders_attending:
            return attending
        else:
            return self.members.none()

    @property
    def size(self):
        """ Return a size of the party """
        return self.members.count()

    def emails(self):
        """ Return a list of unique emails (if any) for leaders of this party """
        return list(set([member.email for member in self.members.all() if member.is_party_leader and member.email]))

    def __unicode__(self):
        return u'{0}'.format(self.name)

#class ResponseCard(models.Model):
#    """ Represent an response card """
#    message = models.TextField(blank=True, help_text='An optional message for the happy couple.')
#    last_updated = models.DateField(auto_now=True)
#
#    def __unicode__(self):
#        return u'<Response card {0}>'.format(self.pk)

class Invitation(models.Model):
    """ Represent an invitation """
    formal_name = models.CharField(max_length=100, blank=False)
    party = models.ForeignKey(Party, unique=True)
    site = models.ForeignKey(Site, default=Site.objects.get_current)
    # response = models.ForeignKey(ResponseCard, unique=True)
    is_viewed = models.BooleanField()
    slug = models.SlugField(max_length=64, blank=False, editable=False, default=create_token)
    response_message = models.TextField(blank=True, help_text='An optional message for the happy couple.')
    last_updated = models.DateField(auto_now=True)
    #last_viewed = models.DateField(null=True)

    class Meta:
        ordering = ['formal_name']

    def get_absolute_url(self):
        return reverse('rsvp-envelope', kwargs={'slug': self.slug})

    def __unicode__(self):
        return u'{0}'.format(self.formal_name)

