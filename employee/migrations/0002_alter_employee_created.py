# Generated by Django 3.2.12 on 2022-03-12 09:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 12, 9, 13, 27, 704015, tzinfo=utc)),
        ),
    ]