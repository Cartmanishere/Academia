# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-25 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Practicals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practical',
            name='objectives',
            field=models.TextField(max_length=5000),
        ),
    ]
