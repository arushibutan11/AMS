# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-26 01:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fir', '0108_auto_20170725_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='ACC_PHOTO4',
        ),
        migrations.RemoveField(
            model_name='details',
            name='ACC_PHOTO5',
        ),
    ]
