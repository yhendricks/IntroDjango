# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 10:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20171109_1200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='authors',
        ),
    ]
