# Generated by Django 4.0.4 on 2022-04-15 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=11)),
                ('email_address', models.CharField(max_length=30)),
                ('street_address', models.CharField(max_length=500)),
                ('allowing', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('sub', models.CharField(max_length=70)),
                ('message', models.CharField(max_length=150)),
                ('allowing', models.BooleanField(default=False)),
            ],
        ),
    ]
