# Generated by Django 4.0.6 on 2024-07-17 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backdoor', '0015_computer_ping_alter_computer_last_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='live',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='ping',
            field=models.CharField(default='0', max_length=100),
        ),
    ]