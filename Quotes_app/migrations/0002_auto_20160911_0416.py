# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Quotes_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_quotes',
            name='quote',
            field=models.CharField(default=datetime.datetime(2016, 9, 11, 1, 12, 6, 983000, tzinfo=utc), max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='daily_quote',
            name='daily_quote',
            field=models.CharField(default=datetime.datetime(2016, 9, 11, 1, 16, 31, 678000, tzinfo=utc), max_length=500),
            preserve_default=False,
        ),
    ]
