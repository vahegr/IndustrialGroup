# Generated by Django 4.0.4 on 2022-06-27 16:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article_app', '0008_alter_article_options_article_created_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 27, 16, 19, 50, 921486, tzinfo=utc)),
        ),
    ]
