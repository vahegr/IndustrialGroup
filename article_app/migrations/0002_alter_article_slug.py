# Generated by Django 4.0.4 on 2022-05-18 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]