# Generated by Django 3.2.12 on 2022-03-30 12:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_project_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 30, 12, 53, 53, 63133, tzinfo=utc)),
        ),
    ]
