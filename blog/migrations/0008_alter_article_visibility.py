# Generated by Django 3.2.12 on 2022-03-31 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('blog', '0007_auto_20220331_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='visibility',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
    ]