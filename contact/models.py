from django.db import models
from django.contrib.sites.models import Site

class ContactRecipient(models.Model):
    """ Represent a recipient """
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=254, blank=False, unique=True)

    def __unicode__(self):
        return u'{0} <{1}>'.format(self.name, self.email)

class ContactPage(models.Model):
    """ Store info about a contact form for a single site """
    site = models.ForeignKey(Site, unique=True)
    recipients = models.ManyToManyField(ContactRecipient, blank=False)
    message_text = models.TextField()
    success_text = models.TextField()
    failure_text = models.TextField()
    # sites = models.ManyToManyField(Site)

    def __unicode__(self):
        return self.site.name

    def recipient_names(self):
        """ Return a pretty-printed list of recipients for display """
        return ', '.join([str(r.name) for r in self.recipients.all()])

    def site_name(self):
        """ Return the name of the site for display """
        return self.site.name

