# Generated by Django 2.0.5 on 2018-09-30 15:17

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
            name='Proposal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
                ('level', models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], max_length=12, verbose_name='Content Level')),
                ('duration', models.DurationField(verbose_name='Duration')),
                ('abstract', models.TextField(verbose_name='Abstract')),
                ('description', models.TextField(verbose_name='Description')),
                ('accepted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Accepted at')),
                ('status', models.CharField(choices=[('retracted', 'Retracted'), ('accepted', 'Accepted'), ('unaccepted', 'Unaccpted'), ('submitted', 'Submitted')], default='submitted', max_length=10, verbose_name='Status')),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Proposal',
                'verbose_name_plural': 'Proposals',
                'db_table': 'proposals',
            },
        ),
        migrations.CreateModel(
            name='ProposalKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=10, verbose_name='Kind')),
            ],
            options={
                'verbose_name': 'Proposal kind',
                'verbose_name_plural': 'Proposal kinds',
                'db_table': 'proposal_details',
            },
        ),
        migrations.AddField(
            model_name='proposal',
            name='kind',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proposals.ProposalKind', verbose_name='Kind'),
        ),
        migrations.AddField(
            model_name='proposal',
            name='speaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Speaker'),
        ),
    ]