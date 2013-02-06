from django.contrib import admin
from rsvp import models

def mark_invited(modeladmin, request, queryset):
    """ Change attributes of selected parties """
    queryset.update(is_invited=True)
mark_invited.short_description = "Mark selected parties as invited"

def mark_uninvited(modeladmin, request, queryset):
    """ Change attributes of selected parties """
    queryset.update(is_invited=False)
mark_uninvited.short_description = "Mark selected parties as uninvited"

def mark_attending(modeladmin, request, queryset):
    """ Change attributes of selected party members """
    queryset.update(is_attending=True)
mark_attending.short_description = "Mark selected party members as invited"

def mark_nonattending(modeladmin, request, queryset):
    """ Change attributes of selected party members """
    queryset.update(is_attending=False)
mark_nonattending.short_description = "Mark selected party members as uninvited"

class PartyAdmin(admin.ModelAdmin):
    list_display = ('name', 'alignment', 'is_invited', 'size', 'is_confirmed', 'headcount', 'last_modified')
    actions = [mark_invited, mark_uninvited]

class PartyMemberAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('name', 'email', 'is_party_leader')}),
        ('Response card', {'fields' : ('is_attending',)}),
    )
    list_display = ('name', 'email', 'is_attending', 'is_party_leader')
    actions = [mark_attending, mark_nonattending]

class InvitationAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('party', 'site')}),
        ('Response card', {'fields' : ('is_viewed', 'response_message')}),
    )
    list_display = ('party', 'slug', 'is_viewed')

admin.site.register(models.PartyMember, PartyMemberAdmin)
admin.site.register(models.Party, PartyAdmin)
admin.site.register(models.Invitation, InvitationAdmin)
