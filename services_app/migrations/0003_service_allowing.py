# Generated by Django 4.0.4 on 2022-04-19 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services_app', '0002_alter_service_description_alter_service_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='allowing',
            field=models.BooleanField(default=False),
        ),
    ]