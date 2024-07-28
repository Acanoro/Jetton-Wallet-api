from django.db import models


# Create your models here.
class AdminDashboardModel(models.Model):
    total_users = models.IntegerField(default=0, verbose_name='Общее количество пользователей')
    active_users = models.IntegerField(default=0, verbose_name='Количество активных пользователей')
    total_referrals = models.IntegerField(default=0, verbose_name='Общее количество рефералов')
    total_tasks_completed = models.IntegerField(default=0, verbose_name='Общее количество выполненных заданий')
    total_emission = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Общая эмиссия JETp')

    def __str__(self):
        return f"Admin Dashboard"

    class Meta:
        verbose_name = 'AdminDashboard'
        verbose_name_plural = 'AdminDashboard'

