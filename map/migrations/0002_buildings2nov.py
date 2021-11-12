# Generated by Django 3.0 on 2021-11-02 07:53

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buildings2Nov',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
                ('ward', models.CharField(blank=True, max_length=254, null=True)),
                ('fid_2', models.IntegerField(blank=True, null=True)),
                ('osm_id', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('addrstreet', models.CharField(blank=True, max_length=254, null=True)),
                ('building', models.CharField(blank=True, max_length=254, null=True)),
                ('num_flats', models.IntegerField(blank=True, null=True)),
                ('wings', models.CharField(blank=True, max_length=10, null=True)),
                ('region', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'buildings_2nov',
                'managed': False,
            },
        ),
    ]