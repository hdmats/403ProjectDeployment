# Generated by Django 4.1.2 on 2022-11-16 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bears', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bears',
            name='sighting_photo',
            field=models.ImageField(blank=True, upload_to='photos'),
        ),
    ]
