# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-11-26 13:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0036_auto_20211126_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 11, 26, 16, 52, 37, 655102), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 11, 26, 16, 52, 37, 656102), verbose_name='Дата'),
        ),
    ]
