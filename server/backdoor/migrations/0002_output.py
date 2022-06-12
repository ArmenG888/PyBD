# Generated by Django 4.0.4 on 2022-06-12 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backdoor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command', models.CharField(default='', max_length=2000)),
                ('output', models.CharField(default='', max_length=2000)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backdoor.computer')),
            ],
        ),
    ]
