# Generated by Django 4.0.4 on 2022-07-08 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0010_alter_homeoption_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeoption',
            name='image',
            field=models.ImageField(null=True, upload_to='images/home'),
        ),
    ]
