# Generated by Django 4.0.4 on 2022-06-13 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0002_contactinfo_instagram_contactinfo_whatsapp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactinfo',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='contactinfo',
            name='whatsapp',
        ),
    ]
