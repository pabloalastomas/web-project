from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Content(models.Model):
    TYPES = (
        ('a', 'Movie'),
        ('b', 'Serie'),
    )
    title = models.CharField(max_length=70, verbose_name='Original Title')
    synopsis = models.TextField(verbose_name='Synopsis', blank=True, null=True)
    airdate = models.DateField(verbose_name='Airdate')
    type = models.CharField(choices=TYPES, verbose_name='Content Type', max_length=1)
    id_in_api = models.CharField(max_length=20, verbose_name='Content ID in API')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')
    date_last_update = models.DateTimeField(auto_now=True, verbose_name='Modification Date')

    def __str__(self):
        return self.title

    def type_content(self):
        for type in self.TYPES:
            if self.type in type[0]:
                return type[1]

    type.short_description = 'Content Type'

    class Meta:
        verbose_name = 'Entertainment Content'
        verbose_name_plural = 'Entertainment Content'


class StreamingPlatforms(models.Model):
    name = models.CharField(max_length=70, verbose_name='Platform Name')
    description = models.TextField(verbose_name='Platform Description', blank=True, null=True)
    url = models.URLField(verbose_name='Platform URL')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')
    date_last_update = models.DateTimeField(auto_now=True, verbose_name='Modification Date')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Streaming Platform'
        verbose_name_plural = 'Streaming Platforms'


class PlatformContent(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, verbose_name='Content')
    platform = models.ForeignKey(StreamingPlatforms, on_delete=models.CASCADE, verbose_name='Platform')
    url = models.URLField(verbose_name='Content URL in platform', blank=True, null=True)
    id_in_platform = models.CharField(max_length=100, verbose_name='Content ID in platform', blank=True, null=True)
    description = models.TextField(verbose_name='Description', blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')
    date_last_update = models.DateTimeField(auto_now=True, verbose_name='Modification Date')

    def __str__(self):
        return f'Content: {self.content.title} - Platform: {self.platform.name}'

    class Meta:
        verbose_name = 'Platform Content'
        verbose_name_plural = 'Platforms Contents'


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class Assessment(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, verbose_name='Content to assessment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    value = IntegerRangeField(verbose_name='Rating', min_value=0, max_value=5)
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')
    date_last_update = models.DateTimeField(auto_now=True, verbose_name='Modification Date')

    def __str__(self):
        return f'Rating: {self.value} - Content: {self.content.title} - User: {self.user.id}'

    class Meta:
        verbose_name = 'Assessment'
        verbose_name_plural = 'Assessments'


class StatusUserContent(models.Model):
    TYPES = (
        ('a', 'Watching'),
        ('b', 'Watched'),
        ('c', 'Favourite'),
        ('d', 'Pending'),
    )
    content = models.ForeignKey(Content, on_delete=models.CASCADE, verbose_name='Content to assessment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    type = models.CharField(choices=TYPES, verbose_name='Status', max_length=1)
    review = models.TextField(verbose_name='Review', blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Watched Date')
    date_last_update = models.DateTimeField(auto_now=True, verbose_name='Modification Date')

    def type_select(self):
        for type in self.TYPES:
            if self.type in type[0]:
                return type[1]

    type_select.short_description = 'Status Type'

    def __str__(self):
        return self.content.title

    class Meta:
        verbose_name = 'User Content Relation'
        verbose_name_plural = 'User Content Relations'
