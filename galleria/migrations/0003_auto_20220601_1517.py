# Generated by Django 2.2 on 2022-06-01 15:17

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galleria', '0002_auto_20220531_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image_image'),
        ),
    ]