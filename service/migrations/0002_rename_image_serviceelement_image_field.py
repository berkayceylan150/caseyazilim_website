# Generated by Django 3.2.12 on 2022-03-12 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serviceelement',
            old_name='image',
            new_name='image_field',
        ),
    ]
