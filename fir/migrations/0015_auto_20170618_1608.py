# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fir', '0014_auto_20170618_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehtype1',
            name='VEHDETL',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='vehtype1',
            name='VEHDTL',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='vehtype1',
            name='VEHTYPE',
            field=models.CharField(max_length=5, primary_key=True, serialize=False),
        ),
    ]
