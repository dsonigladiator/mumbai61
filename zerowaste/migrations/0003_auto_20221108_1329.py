# Generated by Django 3.1.5 on 2022-11-08 07:59

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zerowaste', '0002_auto_20221010_0801'),
    ]

    operations = [
        migrations.CreateModel(
            name='P122Buildings14October22',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(blank=True, null=True, srid=4326)),
                ('fid', models.BigIntegerField(blank=True, null=True)),
                ('sac_number', models.CharField(blank=True, max_length=254, null=True)),
                ('wing_name', models.CharField(blank=True, max_length=254, null=True)),
                ('num_flat', models.CharField(blank=True, max_length=254, null=True)),
                ('num_shops', models.CharField(blank=True, max_length=254, null=True)),
                ('num_floors', models.CharField(blank=True, max_length=254, null=True)),
                ('building_n', models.CharField(blank=True, max_length=254, null=True)),
                ('building_t', models.CharField(blank=True, max_length=254, null=True)),
                ('prabhag_no', models.CharField(blank=True, max_length=254, null=True)),
                ('ward_name_field', models.CharField(blank=True, db_column='ward_name_', max_length=254, null=True)),
                ('prop_add', models.CharField(blank=True, max_length=254, null=True)),
                ('cluster', models.CharField(blank=True, max_length=20, null=True)),
                ('clust_nm', models.CharField(blank=True, max_length=50, null=True)),
                ('population', models.BigIntegerField(blank=True, null=True)),
                ('bin_photo', models.CharField(blank=True, max_length=100, null=True)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('date_time', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('qfield_username', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'p122_buildings_14october22',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='MergedBuildings5Sept22',
        ),
        migrations.DeleteModel(
            name='P122Buildings10October22',
        ),
        migrations.AlterField(
            model_name='wastesegregationdetailsrevised2march22',
            name='coll_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
