# Generated by Django 4.0.6 on 2023-02-11 23:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backdoor', '0013_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='last_online',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 11, 23, 1, 4, 620028, tzinfo=utc)),
        ),
    ]