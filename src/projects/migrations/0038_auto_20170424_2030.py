# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-24 20:30
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0037_auto_20170424_1521'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='intervention',
            options={'ordering': ['order'], 'verbose_name': 'Intervention'},
        ),
        migrations.AlterModelOptions(
            name='manager',
            options={'ordering': ['order'], 'verbose_name': 'Pilote'},
        ),
        migrations.AlterModelOptions(
            name='stakeholder',
            options={'ordering': ['order'], 'verbose_name': 'Acteur'},
        ),
        migrations.AlterModelOptions(
            name='theme',
            options={'ordering': ['order'], 'verbose_name': 'Th\xe9matique'},
        ),
        migrations.AlterModelOptions(
            name='trigger',
            options={'ordering': ['order'], 'verbose_name': 'El\xe9ment d\xe9clencheur'},
        ),
        migrations.AddField(
            model_name='department',
            name='geom',
            field=django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='region',
            name='geom',
            field=django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326),
        ),
    ]
