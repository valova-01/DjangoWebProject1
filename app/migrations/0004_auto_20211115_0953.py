# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-11-15 06:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20211109_1307'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date'], 'verbose_name': 'Комментарий', 'verbose_name_plural': 'комментария к статьям блога'},
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.FileField(default='temp.img', upload_to='', verbose_name='Путь к картинке'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 11, 15, 9, 53, 56, 491645), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 11, 15, 9, 53, 56, 492645), verbose_name='Дата'),
        ),
    ]
