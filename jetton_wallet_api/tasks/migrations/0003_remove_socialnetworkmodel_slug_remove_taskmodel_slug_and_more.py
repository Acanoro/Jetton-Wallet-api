# Generated by Django 4.2.14 on 2024-07-28 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialnetworkmodel',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='taskmodel',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='tasktypemodel',
            name='slug',
        ),
    ]
