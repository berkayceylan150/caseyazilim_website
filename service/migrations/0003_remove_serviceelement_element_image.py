# Generated by Django 3.2.12 on 2022-04-01 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_rename_image_serviceelement_image_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceelement',
            name='element_image',
        ),
    ]
