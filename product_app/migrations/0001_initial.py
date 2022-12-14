# Generated by Django 4.0.4 on 2022-06-17 18:25

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('price', models.CharField(max_length=100)),
                ('coverImage', models.ImageField(null=True, upload_to='images/products')),
                ('image', models.ImageField(upload_to='images/products')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', django_extensions.db.fields.AutoSlugField(allow_unicode=True, blank=True, editable=False, populate_from=['title'])),
                ('allowing', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
