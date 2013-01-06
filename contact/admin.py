from django.contrib import admin
from contact.models import ContactPage, ContactRecipient


class ContactFormAdmin(admin.ModelAdmin):
    """ Show the original column (the string representation) along with names """
    list_display = ('__unicode__', 'recipient_names')

admin.site.register(ContactPage, ContactFormAdmin)
admin.site.register(ContactRecipient)
