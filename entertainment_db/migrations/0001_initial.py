# Generated by Django 3.1.7 on 2021-04-04 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import entertainment_db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Original Title')),
                ('synopsis', models.TextField(blank=True, null=True, verbose_name='Synopsis')),
                ('type', models.CharField(choices=[('a', 'Movie'), ('b', 'Serie')], max_length=5, verbose_name='Content Type')),
                ('id_in_api', models.CharField(max_length=20, verbose_name='Content ID in API')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('date_last_update', models.DateTimeField(auto_now=True, verbose_name='Modification Date')),
            ],
            options={
                'verbose_name': 'Entertainment Content',
                'verbose_name_plural': 'Entertainment Content',
            },
        ),
        migrations.CreateModel(
            name='StreamingPlatforms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Platform Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Platform Description')),
                ('url', models.URLField(verbose_name='Platform URL')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('date_last_update', models.DateTimeField(auto_now=True, verbose_name='Modification Date')),
            ],
            options={
                'verbose_name': 'Streaming Platform',
                'verbose_name_plural': 'Streaming Platforms',
            },
        ),
        migrations.CreateModel(
            name='StatusUserContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('a', 'Watching'), ('b', 'Watched'), ('c', 'Favourite'), ('d', 'Pending')], max_length=5, verbose_name='Content Type')),
                ('review', models.TextField(blank=True, null=True, verbose_name='Review')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Watched Date')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entertainment_db.content', verbose_name='Content to assessment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'User Content Relation',
                'verbose_name_plural': 'User Content Relations',
            },
        ),
        migrations.CreateModel(
            name='PlatformContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Content URL in platform')),
                ('id_in_platform', models.CharField(blank=True, max_length=100, null=True, verbose_name='Content ID in platform')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('date_last_update', models.DateTimeField(auto_now=True, verbose_name='Modification Date')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entertainment_db.content', verbose_name='Content')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entertainment_db.streamingplatforms', verbose_name='Platform')),
            ],
            options={
                'verbose_name': 'Streaming Platform',
                'verbose_name_plural': 'Streaming Platforms',
            },
        ),
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', entertainment_db.models.IntegerRangeField(verbose_name='Rating')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('date_last_update', models.DateTimeField(auto_now=True, verbose_name='Modification Date')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entertainment_db.content', verbose_name='Content to assessment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Assessment',
                'verbose_name_plural': 'Assessments',
            },
        ),
    ]
