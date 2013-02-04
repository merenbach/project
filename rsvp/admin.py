from django.contrib import admin
from rsvp import models

def make_invited(modeladmin, request, queryset):
    """ Change attributes of selected parties """
    queryset.update(is_invited=True)
make_invited.short_description = "Mark selected parties as invited"

def make_uninvited(modeladmin, request, queryset):
    """ Change attributes of selected parties """
    queryset.update(is_invited=False)
make_uninvited.short_description = "Mark selected parties as uninvited"

class PartyAdmin(admin.ModelAdmin):
    list_display = ('name', 'alignment', 'token', 'is_invited', 'invitees', 'is_confirmed', 'attending', 'last_modified')
    actions = [make_invited, make_uninvited]

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_attending', 'is_on_inner_envelope')
    actions = [make_invited, make_uninvited]

admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.Party, PartyAdmin)
admin.site.register(models.RSVP)
