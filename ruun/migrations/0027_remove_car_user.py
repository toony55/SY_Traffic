# Generated by Django 4.0.3 on 2022-05-13 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ruun', '0026_car_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='user',
        ),
    ]