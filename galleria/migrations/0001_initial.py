# Generated by Django 4.0.4 on 2022-05-29 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=25)),
                ('image_description', models.TextField(max_length=75)),
                ('image', models.ImageField(upload_to='pictures')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galleria.category')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galleria.location')),
            ],
            options={
                'ordering': ['image_name'],
            },
        ),
    ]
