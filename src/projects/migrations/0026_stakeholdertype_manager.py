# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-27 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0025_auto_20170227_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='stakeholdertype',
            name='manager',
            field=models.BooleanField(default=None),
        ),
    ]