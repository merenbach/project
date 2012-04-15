##from polls.models import Choice
#from contact.models import ContactFormModel
#from django.contrib import admin
#
##class ChoiceInline(admin.TabularInline):
##	model = Choice
##	extra = 3
#
#class ContactFormAdmin(admin.ModelAdmin):
#    fieldsets = [
#            (None, {'fields':    ['get_message', 'post_message', 'sites']}),
#            ]
#    list_display = ('sites',)
#    list_filter = ['pub_date']
#    search_fields = ['title', 'summary', 'description']
#    date_hierarchy = 'pub_date'
#
#admin.site.register(ContactFormModel, ContactFormAdmin)
#
##admin.site.register(Poll)
##admin.site.register(Choice)
