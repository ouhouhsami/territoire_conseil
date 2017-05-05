# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-25 14:45
from __future__ import unicode_literals
import requests

from django.db import migrations


def forward_func(apps, schema_editor):
    Department = apps.get_model("projects", "Department")
    Region = apps.get_model("projects", "Region")
    departements = Department.objects.all()
    for departement in departements:
        r = requests.get('https://geo.api.gouv.fr/departements?code=%s' % (departement.insee))
        data = r.json()[0]
        region_insee = data['codeRegion']
        region = Region.objects.get(insee=region_insee)
        departement.region = region
        departement.save()


def reverse_func(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0040_auto_20170425_1444'),
    ]

    operations = [
        migrations.RunPython(forward_func, reverse_func),
    ]