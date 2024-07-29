from django.db import models

from admin_dashboard.models import AdminDashboardModel
from users.models import CustomUser, ModeratorsModel


# Create your models here.
class TaskTypeModel(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Тип задания')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Тип задания'
        verbose_name_plural = 'Тип задания'


class TaskModel(models.Model):
    related_task_type = models.ForeignKey(
        TaskTypeModel,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Тип задания'
    )

    name = models.CharField(max_length=100, verbose_name='Задания')
    description = models.TextField(max_length=1000, blank=True, null=True, verbose_name='Описание')
    points = models.IntegerField(default=0)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Задания'
        verbose_name_plural = 'Задания'


class TaskModeratorModel(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('claim', 'Claim'),
        ('reject', 'Reject'),
    ]

    related_user = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Пользователь',
        related_name='moderator_user_tasks'
    )
    related_moderator = models.ForeignKey(
        ModeratorsModel,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Модератор',
        related_name='moderated_tasks'
    )
    related_task = models.ForeignKey(
        TaskModel,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Задания'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='in_progress',
        verbose_name='Статус'
    )
    timestamp = models.DateTimeField(verbose_name='Дата добавления')

    def __str__(self):
        return f'TaskModeratorObject'

    def save(self, *args, **kwargs):
        old_status = None
        if self.pk:
            old_status = TaskModeratorModel.objects.get(pk=self.pk).status

        super().save(*args, **kwargs)

        if old_status != 'claim' and self.status == 'claim':
            dashboard, _ = AdminDashboardModel.objects.get_or_create(id=1)
            dashboard.total_tasks_completed += 1
            dashboard.save()

    class Meta:
        verbose_name = 'Ручная проверка'
        verbose_name_plural = 'Ручная проверка'


class SocialNetworkModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название соц сети')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Название соц сети'
        verbose_name_plural = 'Название соц сети'


class SocialTaskModel(models.Model):
    related_task = models.ForeignKey(
        TaskModel,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Задания'
    )
    related_social_network = models.ForeignKey(
        SocialNetworkModel,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Название соц сети'
    )

    link = models.URLField(verbose_name='Ссылка на соц сеть')

    def __str__(self):
        return f'SocialTaskObject'

    class Meta:
        verbose_name = 'SocialTask'
        verbose_name_plural = 'SocialTask'


class UserTaskModel(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('claim', 'Claim'),
        ('reject', 'Reject'),
    ]

    related_user = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Пользователь'
    )

    related_social_task = models.ForeignKey(
        SocialTaskModel,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='SocialTask'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='in_progress',
        verbose_name='Статус'
    )
    timestamp = models.DateTimeField(verbose_name='Дата добавления')

    def __str__(self):
        return f'UserTaskObject'

    def save(self, *args, **kwargs):
        old_status = None
        if self.pk:
            old_status = UserTaskModel.objects.get(pk=self.pk).status

        super().save(*args, **kwargs)

        if old_status != 'claim' and self.status == 'claim':
            dashboard, _ = AdminDashboardModel.objects.get_or_create(id=1)
            dashboard.total_tasks_completed += 1
            dashboard.save()

    class Meta:
        verbose_name = 'UserTask'
        verbose_name_plural = 'UserTask'
