# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fir', '0040_auto_20170620_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='DUPL',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='details',
            name='INJBOY',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='INJFEMALE',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='INJGIRL',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='INJMALE',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='INJURED',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='KILBOY',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='KILFEMALE',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='KILGIRL',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='KILLED',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='KILMALE',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='PEDESTRIAN',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='PENDING',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
