# Generated by Django 4.0.3 on 2022-05-08 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruun', '0010_alter_car_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='baalance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.DeleteModel(
            name='Balance',
        ),
    ]
