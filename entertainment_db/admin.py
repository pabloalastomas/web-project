from django import forms
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


class StreamingPlatformsAdmin(admin.ModelAdmin):
    readonly_fields = ('date_creation', 'date_last_update')
    list_display = ('name', 'url', 'date_creation', 'date_last_update')
    ordering = ['name']
    empty_value_display = 'Empty data'


admin.site.register(StreamingPlatforms, StreamingPlatformsAdmin)


class PlatformContentAdmin(admin.ModelAdmin):
    readonly_fields = ('date_creation', 'date_last_update')
    list_display = ('content', 'get_content_type', 'platform', 'id_in_platform', 'date_last_update')
    ordering = ['content', 'platform']
    empty_value_display = 'Empty data'

    def get_content_type(self, obj):
        return obj.content.type_content()

    get_content_type.short_description = 'Content Type'


admin.site.register(PlatformContent, PlatformContentAdmin)


class AssessmentAdmin(admin.ModelAdmin):
    readonly_fields = ('date_creation', 'date_last_update')
    list_display = ('content', 'user', 'value', 'date_creation', 'date_last_update')
    ordering = ['content']
    empty_value_display = 'Empty data'


admin.site.register(Assessment, AssessmentAdmin)


class StatusUserContentForm(
    forms.ModelForm):  # Form to validate there is not multiple entrey with same content and user.
    class Meta:
        model = StatusUserContent
        fields = '__all__'

    def clean(self):
        if self.instance.pk is None:  # add
            if StatusUserContent.objects.filter(content=self.cleaned_data['content'],
                                                user=self.cleaned_data['user']).exists():
                raise ValidationError(
                    'A status has already defined for this content and user. To change the status edit the existing entry.')


class StatusUserContentAdmin(admin.ModelAdmin):
    form = StatusUserContentForm
    readonly_fields = ('date_creation', 'date_last_update')
    list_display = ('content', 'user', 'type_select', 'date_creation', 'date_last_update')
    ordering = ['content']
    empty_value_display = 'Empty data'


admin.site.register(StatusUserContent, StatusUserContentAdmin)
