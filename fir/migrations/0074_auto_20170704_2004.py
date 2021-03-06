# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 14:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fir', '0073_auto_20170704_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='ROAD_ENGG_FAULT',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fir.road_engg_fault', verbose_name='Road Engg'),
        ),
        migrations.AlterField(
            model_name='details',
            name='ROAD_ENV_FAULT',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fir.road_env_fault', verbose_name='Road Environment'),
        ),
        migrations.AlterField(
            model_name='details',
            name='VEH_MECH_FAULT',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fir.veh_mech_fault', verbose_name='Vehicle Mechanical'),
        ),
        migrations.AlterField(
            model_name='details',
            name='VICTIM_FAULT',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fir.victim_fault', verbose_name='Victim'),
        ),
        migrations.AlterField(
            model_name='details',
            name='WEATHER_COND',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fir.weather_cond', verbose_name='Weather Cond'),
        ),
    ]
