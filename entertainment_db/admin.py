from django.contrib import admin
from entertainment_db.models import *

# Register your models here.

admin.site.site_header = 'Entertainment Database'  # Change Django Admin Title


class ContentAdmin(admin.ModelAdmin):
    readonly_fields = ('date_creation', 'date_last_update')
    list_display = ('title', 'type_content', 'id_in_api', 'airdate', 'date_creation')
    ordering = ['id']
    empty_value_display = 'Empty data'


admin.site.register(Content, ContentAdmin)
