from django import forms
from django.contrib import admin, messages
from django.core.exceptions import ValidationError

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


class PlatformContentForm(
    forms.ModelForm):  # Form to validate there is not multiple entrey with same content and user.
    class Meta:
        model = PlatformContent
        fields = '__all__'

    def clean(self):
        if self.instance.pk is None:  # add
            if PlatformContent.objects.filter(content=self.cleaned_data['content'],
                                              platform=self.cleaned_data['platform']).exists():
                error = "A connection has already been defined for this content. To change this edit the existing " \
                        "entry. "
                error2 = "A connection has already been defined for this platform. To change this edit the existing " \
                         "entry. "
                raise ValidationError({'content': [error], 'platform': [error2]})


class PlatformContentAdmin(admin.ModelAdmin):
    form = PlatformContentForm
    readonly_fields = ('date_creation', 'date_last_update')
    list_display = ('content', 'get_content_type', 'platform', 'id_in_platform', 'date_last_update')
    ordering = ['content', 'platform']
    empty_value_display = 'Empty data'

    def get_content_type(self, obj):
        return obj.content.type_content()

    get_content_type.short_description = 'Content Type'


admin.site.register(PlatformContent, PlatformContentAdmin)


class AssessmentForm(forms.ModelForm):  # Form to validate there is not multiple entry with same content and user.
    class Meta:
        model = Assessment
        fields = '__all__'

    def clean(self):
        if self.instance.pk is None:  # add
            if Assessment.objects.filter(content=self.cleaned_data['content'],
                                         user=self.cleaned_data['user']).exists():
                error = "A rating has already been defined for this content. To change this edit the existing entry."
                error2 = "A rating has already been defined for this user. To change this edit the existing entry."
                raise ValidationError({'content': [error], 'user': [error2]})


class AssessmentAdmin(admin.ModelAdmin):
    form = AssessmentForm
    readonly_fields = ('date_creation', 'date_last_update')
    list_display = ('content', 'user', 'rating', 'date_creation', 'date_last_update')
    ordering = ['content']
    empty_value_display = 'Empty data'


admin.site.register(Assessment, AssessmentAdmin)


class StatusUserContentForm(
    forms.ModelForm):  # Form to validate there is not multiple entry with same content and user.
    class Meta:
        model = StatusUserContent
        fields = '__all__'

    def clean(self):
        if self.instance.pk is None:  # add
            if StatusUserContent.objects.filter(content=self.cleaned_data['content'],
                                                user=self.cleaned_data['user']).exists():
                error = "A status has already been defined for this content. To change this edit the existing entry."
                error2 = "A status has already been defined for this user. To change this edit the existing entry."
                raise ValidationError({'content': [error], 'user': [error2]})


class StatusUserContentAdmin(admin.ModelAdmin):
    form = StatusUserContentForm
    readonly_fields = ('date_creation', 'date_last_update')
    list_display = ('content', 'user', 'type_select', 'date_creation', 'date_last_update')
    ordering = ['content']
    empty_value_display = 'Empty data'


admin.site.register(StatusUserContent, StatusUserContentAdmin)
