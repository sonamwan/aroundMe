# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-11 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_remove_event_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_date',
            field=models.CharField(default='', max_length=30),
        ),
    ]