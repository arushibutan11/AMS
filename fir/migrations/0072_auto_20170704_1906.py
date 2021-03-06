# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 13:36
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('fir', '0071_auto_20170704_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='ACC_PHOTO',
            field=models.FileField(blank=True, default='', upload_to='documents/', verbose_name='Accident Photo'),
        ),
        migrations.AlterField(
            model_name='details',
            name='ACC_SKETCH_PHOTO',
            field=models.FileField(blank=True, default='', upload_to='documents/', verbose_name='Sketch Photo'),
        ),
        migrations.AlterField(
            model_name='details',
            name='AREA',
            field=models.CharField(choices=[('URBAN', 'URBAN'), ('RURAL', 'RURAL')], max_length=30, verbose_name='Area'),
        ),
        migrations.AlterField(
            model_name='details',
            name='AREA_TYPE',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fir.area_type', verbose_name='Area Type'),
        ),
        migrations.AlterField(
            model_name='details',
            name='AREA_TYPE2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fir.area_type2', verbose_name='Area Type 2'),
        ),
        migrations.AlterField(
            model_name='details',
            name='AREA_TYPE2_OTHER',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='fir.area_type2_oth', verbose_name='Area Type 2 Other'),
        ),
        migrations.AlterField(
            model_name='details',
            name='AREA_TYPE_OTHER',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Area Type Other'),
        ),
        migrations.AlterField(
            model_name='details',
            name='CIRCLE',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fir.circles', verbose_name='Circle'),
        ),
        migrations.AlterField(
            model_name='details',
            name='DATE_OCC',
            field=models.DateField(verbose_name='Accident Date'),
        ),
        migrations.AlterField(
            model_name='details',
            name='DIST',
            field=models.CharField(max_length=5, verbose_name='District'),
        ),
        migrations.AlterField(
            model_name='details',
            name='FIRNO',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(1)], verbose_name='FIR No.'),
        ),
        migrations.AlterField(
            model_name='details',
            name='FIR_PHOTO',
            field=models.FileField(blank=True, default='', upload_to='documents/', verbose_name='FIR Photo'),
        ),
        migrations.AlterField(
            model_name='details',
            name='FLYOVER_UNDERPASS',
            field=models.CharField(blank=True, choices=[('Ascending Flyover', 'Ascending Flyover'), ('Descending Flyover', 'Descending Flyover'), ('Ascending Flyover Loop', 'Ascending Flyover Loop'), ('Descending Flyover Loop', 'Desscending Flyover Loop')], max_length=30, verbose_name='Flyover/Underpass'),
        ),
        migrations.AlterField(
            model_name='details',
            name='GROUND_LEVEL',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='fir.ground_level', verbose_name='Ground Level'),
        ),
        migrations.AlterField(
            model_name='details',
            name='JUNCTION_CONTROL',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fir.junction_control', verbose_name='Junction'),
        ),
        migrations.AlterField(
            model_name='details',
            name='LOCATION',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='fir.location', verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='details',
            name='MINORROADNAME',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Minor Road Name'),
        ),
        migrations.AlterField(
            model_name='details',
            name='MVA_NAME',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='fir.mva_act', verbose_name='MVA'),
        ),
        migrations.AlterField(
            model_name='details',
            name='OF_SECTION',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fir.sections', verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='details',
            name='PLACE_OCC',
            field=models.CharField(blank=True, default='', max_length=140, verbose_name='Place of Occurence'),
        ),
        migrations.AlterField(
            model_name='details',
            name='PS',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='CIRCLE', chained_model_field='CIRCLE', on_delete=django.db.models.deletion.CASCADE, to='fir.policestation', verbose_name='Police Station'),
        ),
        migrations.AlterField(
            model_name='details',
            name='RNG',
            field=models.CharField(max_length=5, verbose_name='Range'),
        ),
        migrations.AlterField(
            model_name='details',
            name='ROAD',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='CIRCLE', chained_model_field='CIRCLE', on_delete=django.db.models.deletion.CASCADE, to='fir.roads', verbose_name='Road'),
        ),
        migrations.AlterField(
            model_name='details',
            name='ROADNAME',
            field=models.CharField(max_length=150, verbose_name='Road Name'),
        ),
        migrations.AlterField(
            model_name='details',
            name='ROAD_LEVEL',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fir.road_level', verbose_name='Road Level'),
        ),
        migrations.AlterField(
            model_name='details',
            name='TIME_KNOWN',
            field=models.CharField(choices=[('Y', 'YES'), ('N', 'NO')], max_length=30, verbose_name='Time Known'),
        ),
        migrations.AlterField(
            model_name='details',
            name='TIME_OCC',
            field=models.CharField(blank=True, default='', max_length=4, verbose_name='Time'),
        ),
    ]
