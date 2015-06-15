# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 15, 20, 2, 9, 93621, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
