# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fir', '0036_auto_20170620_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='INJBOY',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='details',
            name='INJFEMALE',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='details',
            name='INJGIRL',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='details',
            name='INJMALE',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='details',
            name='INJURED',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='details',
            name='KILBOY',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='details',
            name='KILFEMALE',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='details',
            name='KILGIRL',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='details',
            name='KILLED',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='details',
            name='KILMALE',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='details',
            name='PEDESTRIAN',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
