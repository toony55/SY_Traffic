# Generated by Django 4.0.3 on 2022-05-01 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ruun', '0008_alter_car_driver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drri', to='ruun.driver'),
        ),
    ]