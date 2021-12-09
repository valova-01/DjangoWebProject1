# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-08 16:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='nickname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Логин'),
        ),
    ]
