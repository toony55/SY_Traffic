# Generated by Django 4.0.3 on 2022-05-12 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruun', '0018_insurance_user_license_user_violations_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='mmm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cc', models.CharField(default='', help_text='Type Of cc.', max_length=50)),
                ('nn', models.CharField(default='', help_text='Number Of nn', max_length=30)),
            ],
        ),
    ]
