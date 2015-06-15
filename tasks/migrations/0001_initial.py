# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField(null=True)),
                ('created', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('revision', models.IntegerField()),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('foreword', models.TextField(null=True)),
                ('description', models.TextField()),
                ('time_limit', models.IntegerField()),
                ('updated', models.DateTimeField()),
                ('revision', models.IntegerField(default=1)),
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
