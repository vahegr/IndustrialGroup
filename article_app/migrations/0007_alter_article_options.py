# Generated by Django 4.0.4 on 2022-06-17 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article_app', '0006_remove_article_visits'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-created',)},
        ),
    ]
