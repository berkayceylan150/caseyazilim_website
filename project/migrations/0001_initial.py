# Generated by Django 3.2.12 on 2022-03-12 09:13

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='project_images')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('not_software_project', models.BooleanField(default=False)),
                ('language_technologies', models.TextField(blank=True)),
                ('short_detail', models.CharField(blank=True, max_length=150)),
                ('detail', tinymce.models.HTMLField(blank=True)),
                ('created', models.DateTimeField(default=datetime.datetime(2022, 3, 12, 9, 13, 22, 541871, tzinfo=utc))),
                ('images', models.ManyToManyField(blank=True, default=[0], to='project.Image')),
                ('main_image', models.ForeignKey(blank=True, default=[0], on_delete=django.db.models.deletion.CASCADE, related_name='project_main_image', to='project.image')),
                ('service', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='service.service')),
            ],
        ),
    ]
