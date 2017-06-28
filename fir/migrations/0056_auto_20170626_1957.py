# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-26 14:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fir', '0055_auto_20170626_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='userprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='0', max_length=50)),
                ('username', models.CharField(default='', max_length=20)),
                ('emp_id', models.CharField(default='0', max_length=15)),
                ('district_circle', models.CharField(blank=True, max_length=30)),
                ('range_circle', models.CharField(blank=True, max_length=30)),
                ('designation', models.CharField(choices=[('DCP', 'DCP'), ('ACP', 'ACP'), ('INSPECTOR', 'INSPECTOR'), ('ACCIDENT RESEARCH CELL', 'ACCIDENT RESEARCH CELL')], max_length=30)),
                ('password1', models.CharField(blank=True, max_length=30)),
                ('password2', models.CharField(blank=True, max_length=30)),
                ('circle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fir.circles')),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='circle',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='profile',
        ),
    ]