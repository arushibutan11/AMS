# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-26 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fir', '0057_auto_20170626_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='circle',
            field=models.CharField(default='0', max_length=15),
        ),
    ]