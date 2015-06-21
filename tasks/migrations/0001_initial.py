# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
from django.conf import settings
import tasks.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('uid', models.UUIDField(default=uuid.uuid4, unique=True, editable=False, db_index=True)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('taken', models.DateTimeField(null=True)),
            ],
            options={
                'ordering': ['-created'],
                'db_table': 'assignments',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('foreword', models.TextField(null=True)),
                ('description', models.TextField()),
                ('time_limit', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('attachment', models.FileField(upload_to=tasks.models.get_attachment_path)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated'],
                'db_table': 'tasks',
            },
        ),
        migrations.AddField(
            model_name='assignment',
            name='task',
            field=models.ForeignKey(to='tasks.Task'),
        ),
    ]
