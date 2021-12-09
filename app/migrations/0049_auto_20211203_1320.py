# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-03 10:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0048_auto_20211201_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 3, 13, 20, 20, 65575), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 3, 13, 20, 20, 66575), verbose_name='Дата'),
        ),
    ]