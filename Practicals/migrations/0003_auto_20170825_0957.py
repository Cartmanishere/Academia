# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-25 04:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Practicals', '0002_auto_20170825_0742'),
    ]

    operations = [
        migrations.RenameField(
            model_name='practical',
            old_name='title',
            new_name='aim',
        ),
    ]
