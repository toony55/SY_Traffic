# Generated by Django 4.0.3 on 2022-05-12 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ruun', '0021_remove_violations_plate'),
    ]

    operations = [
        migrations.AddField(
            model_name='violations',
            name='plate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ruun.car'),
        ),
    ]
