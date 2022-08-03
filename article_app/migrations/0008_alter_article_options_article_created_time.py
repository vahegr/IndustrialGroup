# Generated by Django 4.0.4 on 2022-06-27 16:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article_app', '0007_alter_article_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-created_time',)},
        ),
        migrations.AddField(
            model_name='article',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
