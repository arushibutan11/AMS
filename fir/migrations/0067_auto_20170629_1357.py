# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 13:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fir', '0066_auto_20170629_0443'),
    ]

    operations = [
        migrations.CreateModel(
            name='area_type2',
            fields=[
                ('SAtype_Code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('SArea_Type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='area_type2_oth',
            fields=[
                ('SOAtype_Code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('SOArea_Type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ground_level',
            fields=[
                ('RL_Code', models.CharField(max_length=20)),
                ('RL_Name', models.CharField(max_length=100)),
                ('GL_Code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('GL_Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='junction_control',
            fields=[
                ('GL_Code', models.CharField(max_length=20)),
                ('GL_Name', models.CharField(max_length=100)),
                ('JCTRL_Code', models.CharField(max_length=20)),
                ('JCTRL_Name', models.CharField(max_length=100)),
                ('GL_JCTRL_Code', models.CharField(default='0', max_length=40, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='mva_act',
            fields=[
                ('MVA_Section', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('MVA_Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='road_type',
            fields=[
                ('RT_Code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('RT_Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='road_type1',
            fields=[
                ('SRT_Code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('SRT_Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='victim_person_status1',
            fields=[
                ('Victim_Person_Status1', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='circle',
            field=models.CharField(choices=[('', '-----------'), ('PGC', 'PAHAR GANJ CIRCLE'), ('KBC', 'KAROL BAGH CIRCLE'), ('KMC', 'KAMLA MARKET CIRCLE'), ('DGC', 'DARYA GANJ CIRCLE'), ('KPC', 'KALYAN PURI CIRCLE'), ('VKC', 'VIVEK VIHAR CIRCLE'), ('MWC', 'MANDAWALI CIRCLE'), ('GNC', 'GANDHI NAGAR CIRCLE'), ('KOT', 'KOTWALI CIRCLE'), ('CLC', 'CIVIL LINES CIRCLE'), ('SBC', 'SADAR BAZAR CIRCLE'), ('SMC', 'SABZI MANDI CIRCLE'), ('PTC', 'PARLIAMENT STREET CIRCLE'), ('TRC', 'TUGHLAK ROAD CIRCLE'), ('PTH', 'PARLIAMENT HOUSE CIRCLE'), ('TMC', 'TILAK MARG CIRCLE'), ('CHP', 'CHANAKYA PURI CIRCLE'), ('BKR', 'BARA KHAMBA ROAD CIRCLE'), ('SHD', 'SHAHDARA CIRCLE'), ('SLC', 'KHAZOORI CIRCLE'), ('SPC', 'SEEMA PURI CIRCLE'), ('MTC', 'MODEL TOWN CIRCLE'), ('NRL', 'BURARI CIRCLE'), ('AVC', 'ASHOK VIHAR CIRCLE'), ('ALP', 'NARELA CIRCLE'), ('BWC', 'BAWANA CIRCLE'), ('RHN', 'ROHINI CIRCLE'), ('MGP', 'MANGOL PURI CIRCLE'), ('IGI', 'I.G. AIR PORT CIRCLE'), ('PAP', 'PALAM AIRPORT CIRCLE'), ('DRP', 'DELHI RAILWAYS CIRCLE'), ('RKP', 'R.K. PURAM CIRCLE'), ('DFC', 'DEFENCE COLONY CIRCLE'), ('DCC', 'DELHI CANTT CIRCLE'), ('VVC', 'VASANT VIHAR CIRCLE'), ('SDV', 'SUKHDEV VIHAR CIRCLE'), ('LNC', 'LAJPAT NAGAR CIRCLE'), ('HKC', 'HAUS KHAS CIRCLE'), ('SVC', 'SARITA VIHAR CIRCLE'), ('KKC', 'KALKAJI CIRCLE'), ('SGV', 'SANGAM VIHAR CIRCLE'), ('SKT', 'SAKET CIRCLE'), ('GKC', 'GREATER KAILASH CIRCLE'), ('MRC', 'MEHRAULI CIRCLE'), ('KHC', 'KAPASHERA CIRCLE'), ('DWC', 'DWARKA CIRCLE'), ('TNC', 'TILAK NAGAR CIRCLE'), ('NJC', 'NAJAF GARH CIRCLE'), ('JPC', 'JANAK PURI CIRCLE'), ('NLC', 'NANGLOI CIRCLE'), ('PNC', 'PATEL NAGAR CIRCLE'), ('MPC', 'MAYA PURI CIRCLE'), ('PBC', 'PUNJABI BAGH CIRCLE'), ('RGC', 'RAJOURI GARDEN CIRCLE')], max_length=60),
        ),
        migrations.AlterField(
            model_name='profile',
            name='designation',
            field=models.CharField(choices=[('', '-----------'), ('DCP', 'DCP'), ('ACP', 'ACP'), ('INS', 'INSPECTOR'), ('ARC', 'ACCIDENT RESEARCH CELL')], max_length=30),
        ),
        migrations.AddField(
            model_name='details',
            name='GROUND_LEVEL',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='fir.ground_level'),
        ),
        migrations.AddField(
            model_name='details',
            name='JUNCTION_CONTROL',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='fir.junction_control'),
        ),
        migrations.AddField(
            model_name='details',
            name='MVA_NAME',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='fir.mva_act'),
        ),
        migrations.AddField(
            model_name='details',
            name='ROAD_TYPE',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='fir.road_type'),
        ),
        migrations.AddField(
            model_name='details',
            name='ROAD_TYPE1',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='fir.road_type1'),
        ),
        migrations.AddField(
            model_name='details',
            name='SAREA_TYPE',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='fir.area_type2'),
        ),
        migrations.AddField(
            model_name='details',
            name='SOAREA_TYPE',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='fir.area_type2_oth'),
        ),
        migrations.AddField(
            model_name='details',
            name='VICTIM_PERSON_STATUS1',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='fir.victim_person_status1'),
        ),
    ]
