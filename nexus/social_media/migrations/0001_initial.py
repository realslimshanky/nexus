# Generated by Django 2.0.5 on 2018-08-31 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('posted_at', models.CharField(choices=[('fb', 'Facebook'), ('twitter', 'Twitter'), ('linkedin', 'Linkedin')], max_length=10, verbose_name='Posted at platform')),
                ('posted_time', models.DateTimeField(null=True, verbose_name='Posted at')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='Content Image')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Content Text')),
                ('is_approved', models.BooleanField(default=False, help_text='is the post approved by Nexus administrator?', verbose_name='Is post approved')),
                ('is_posted', models.BooleanField(default=False, help_text='is the post published?', verbose_name='Is posted')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Posted by')),
                ('scheduled_time', models.DateTimeField(null=True, verbose_name='Scheduled at')),
                ('approval_time', models.DateTimeField(null=True, verbose_name='Approved at')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]