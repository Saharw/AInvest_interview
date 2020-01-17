# Generated by Django 3.0.2 on 2020-01-17 04:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='update_time',
        ),
        migrations.AlterField(
            model_name='client',
            name='register_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
