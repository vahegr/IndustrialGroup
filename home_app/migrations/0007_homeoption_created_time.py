# Generated by Django 4.0.4 on 2022-07-05 07:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0006_temporarypost'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeoption',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
