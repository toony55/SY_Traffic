# Generated by Django 4.0.3 on 2022-05-13 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruun', '0029_remove_license_plate_license_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='license',
            name='photo',
            field=models.URLField(default=''),
        ),
    ]
