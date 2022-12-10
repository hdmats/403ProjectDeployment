# Generated by Django 4.1.2 on 2022-11-16 16:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bears',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bear_type', models.CharField(max_length=20)),
                ('bear_age', models.CharField(max_length=20)),
                ('bear_count', models.IntegerField(default=1)),
                ('sighting_date', models.DateField(blank=True, default=datetime.datetime.today)),
                ('sighting_time', models.TimeField(blank=True, default=datetime.datetime.today)),
                ('sighting_location', models.CharField(max_length=50)),
                ('sighting_photo', models.ImageField(upload_to='photos')),
                ('sighting_notes', models.CharField(max_length=200)),
            ],
        ),
    ]
