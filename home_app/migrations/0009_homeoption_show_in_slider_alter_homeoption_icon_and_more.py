# Generated by Django 4.0.4 on 2022-07-08 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0008_alter_homeoption_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeoption',
            name='show_in_slider',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='homeoption',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to='images/home/icons'),
        ),
        migrations.AlterField(
            model_name='homeoption',
            name='second_title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='homeoption',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='homeoption',
            name='url',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]