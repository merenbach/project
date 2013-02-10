from django.contrib import admin
from rsvp import models

def mark_viewed(modeladmin, request, queryset):
    """ Change attributes of selected parties """
    queryset.update(is_viewed=True)
mark_viewed.short_description = "Mark selected invitations as viewed"

def mark_unviewed(modeladmin, request, queryset):
    """ Change attributes of selected parties """
    queryset.update(is_viewed=False)
mark_unviewed.short_description = "Mark selected invitations as unviewed"

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
mark_attending.short_description = "Mark selected party members as attending"

def mark_nonattending(modeladmin, request, queryset):
    """ Change attributes of selected party members """
    queryset.update(is_attending=False)
mark_nonattending.short_description = "Mark selected party members as nonattending"

class PartyAdmin(admin.ModelAdmin):
    list_display = ('name', 'alignment', 'is_invited', 'size', 'is_confirmed', 'headcount', 'last_modified')
    actions = (mark_invited, mark_uninvited)

class InviteeAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('name', 'email', 'is_party_leader')}),
        ('Response card', {'fields' : ('is_attending',)}),
    )
    list_display = ('name', 'email', 'is_attending', 'is_party_leader')
    actions = (mark_attending, mark_nonattending)

class InvitationAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('party', 'formal_name', 'site')}),
        ('Invitation', {'fields' : ('is_viewed',)}),
        ('Response card', {'fields' : ('response_message',)}),
    )
    list_display = ('party', 'formal_name', 'slug', 'is_viewed')
    actions = (mark_viewed, mark_unviewed)
    # prepopulated_fields = {'formal_name': ('party',)}

admin.site.register(models.Invitee, InviteeAdmin)
admin.site.register(models.Party, PartyAdmin)
admin.site.register(models.Invitation, InvitationAdmin)
