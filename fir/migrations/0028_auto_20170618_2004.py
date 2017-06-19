# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 20:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fir', '0027_auto_20170618_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='self_type',
            fields=[
                ('SNO', models.CharField(max_length=100)),
                ('CODE', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('TYPE', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='details',
            name='SELF_TYPE',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fir.self_type'),
        ),
        migrations.AlterField(
            model_name='details',
            name='routeno',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
