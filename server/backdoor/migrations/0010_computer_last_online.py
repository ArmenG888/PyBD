# Generated by Django 4.0.4 on 2022-06-14 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backdoor', '0009_image_img_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='last_online',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
