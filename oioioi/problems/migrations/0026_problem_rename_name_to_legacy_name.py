# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-05-10 09:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0025_difficulty_tag_proposal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='problem',
            old_name='name',
            new_name='legacy_name',
        ),
    ]
