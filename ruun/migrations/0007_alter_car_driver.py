# Generated by Django 4.0.3 on 2022-05-01 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ruun', '0006_alter_driver_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ruun.driver'),
        ),
    ]
