# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 15:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fir', '0035_auto_20170620_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='SELF_TYPE',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fir.self_type'),
        ),
    ]