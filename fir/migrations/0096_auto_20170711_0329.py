# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 03:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fir', '0095_offender_dri_lic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offender',
            name='SUBVEHICLE_TYPE1',
            field=models.CharField(blank=True, choices=[('Scooter', 'Scooter'), ('Scooty', 'Scooty'), ('Motor bike', 'Motor bike')], default='', max_length=15, verbose_name='Sub Vehicle Type'),
        ),
        #migrations.AlterField(
         #   model_name='victim_person',
          #  name='VEH_INFO',
           # field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fir.vehtype1', verbose_name='Vehicle Info'),
        #),
        migrations.AlterField(
            model_name='victim_vehicle',
            name='SUBVEHICLE_TYPE2',
            field=models.CharField(blank=True, choices=[('Scooter', 'Scooter'), ('Scooty', 'Scooty'), ('Motor bike', 'Motor bike')], default=0, max_length=15, verbose_name='Sub Vehicle Type'),
        ),
    ]
