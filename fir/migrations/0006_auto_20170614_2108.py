# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 15:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fir', '0005_auto_20170614_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roads',
            name='CIRCLE',
        ),
        migrations.AddField(
            model_name='roads',
            name='CIRCLE',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='fir.circles'),
            preserve_default=False,
        ),
    ]