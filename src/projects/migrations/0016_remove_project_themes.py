# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-27 15:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20170127_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='themes',
        ),
    ]
