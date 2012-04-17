from software.models import Software
from django.contrib import admin

#class ChoiceInline(admin.TabularInline):
#	model = Choice
#	extra = 3

class SoftwareAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {'fields':    ['title', 'version', 'slug', 'summary', 'is_published', 'tags', 'description']}),
            ('File information', {'fields' : ['app_file', 'src_file']}),
            ('Date information', {'fields' : ['pub_date'], 'classes': ['collapse']}),
            ]
    #inlines = [ChoiceInline]
    list_display = ('title', 'version', 'summary', 'pub_date', 'is_published')
    list_filter = ['pub_date']
    search_fields = ['title', 'summary', 'description']
    date_hierarchy = 'pub_date'

admin.site.register(Software, SoftwareAdmin)

#admin.site.register(Poll)
#admin.site.register(Choice)
