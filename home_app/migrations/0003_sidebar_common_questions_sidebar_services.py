# Generated by Django 4.0.4 on 2022-06-27 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0002_homeoptions'),
    ]

    operations = [
        migrations.AddField(
            model_name='sidebar',
            name='common_questions',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sidebar',
            name='services',
            field=models.BooleanField(default=False),
        ),
    ]
