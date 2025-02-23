# Generated by Django 4.2.14 on 2024-07-29 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminDashboardModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_users', models.IntegerField(default=0, verbose_name='Общее количество пользователей')),
                ('active_users', models.IntegerField(default=0, verbose_name='Количество активных пользователей')),
                ('total_referrals', models.IntegerField(default=0, verbose_name='Общее количество рефералов')),
                ('total_tasks_completed', models.IntegerField(default=0, verbose_name='Общее количество выполненных заданий')),
                ('total_emission', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Общая эмиссия JETp')),
            ],
            options={
                'verbose_name': 'AdminDashboard',
                'verbose_name_plural': 'AdminDashboard',
            },
        ),
    ]
