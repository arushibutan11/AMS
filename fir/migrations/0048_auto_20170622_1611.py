# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 16:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fir', '0047_auto_20170622_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='ACCAGE',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='ACCSEX',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='ACCTYPE',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='BLACK_SPOT',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='BLACK_SPOT_NO',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='BRIEF_FACTS',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='BUS_NO',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='CATEGORY',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='CN_DT',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='CONFIRM',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='CONVERT_FN',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='DUPL',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='FOR_BLK',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='F_STATUS',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='HIT_AND_RUN_UPDATE1',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='Intersection',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='LONGITUDE',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='details',
            name='PENDING',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='PILLION_HELMET',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='REMARK',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='RIDER_HELMET',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='RNOV1A',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='RNOV1B',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='RNOV2A',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='RNOV2B',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='SCANNED',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='SELF_TYPE',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='fir.self_type'),
        ),
        migrations.AlterField(
            model_name='details',
            name='STATE',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='STATUS',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='TIME_OCC',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='TWW1',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='TWW2',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='VICTIM',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='case_status',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='convert_case',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='dri_add',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='dri_add1',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='dri_arrest',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='dri_fath',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='dri_lic_no',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='dri_lic_status',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='dri_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='dri_place',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='dri_sex',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='routeno',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
