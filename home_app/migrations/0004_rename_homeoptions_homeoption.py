# Generated by Django 4.0.4 on 2022-06-27 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0003_sidebar_common_questions_sidebar_services'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HomeOptions',
            new_name='HomeOption',
        ),
    ]