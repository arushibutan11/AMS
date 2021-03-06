# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fir', '0028_auto_20170618_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='CONVERT',
            field=models.CharField(choices=[('T', 'TRUE'), ('F', 'FALSE')], max_length=15),
        ),
        migrations.AlterField(
            model_name='details',
            name='dri_arrest',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=15),
        ),
        migrations.AlterField(
            model_name='self_type',
            name='SNO',
            field=models.CharField(max_length=20),
        ),
    ]
