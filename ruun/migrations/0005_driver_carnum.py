# Generated by Django 4.0.3 on 2022-04-07 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruun', '0004_car_violnum'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='carnum',
            field=models.CharField(default='', max_length=30, verbose_name='The Number of Cars Owned By The Driver'),
        ),
    ]
