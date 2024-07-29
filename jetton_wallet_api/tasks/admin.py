from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from tasks.models import *


# Register your models here.
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    search_fields = ('name',)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'points', 'status')
    search_fields = ('name', 'description',)
    list_filter = ('status',)


class TaskModeratorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user_link', 'status', 'timestamp',)
    search_fields = ('related_user__username',)
    list_filter = ('status',)

    def user_link(self, obj):
        url = reverse('admin:users_customuser_change', args=[obj.related_user_id])
        return format_html(f'<a href="{url}">{obj.related_user}</a>')

    user_link.short_description = 'Пользователь'


class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    search_fields = ('name',)


class SocialTaskAdmin(admin.ModelAdmin):
    pass


class UserTaskAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user_link', 'status', 'timestamp',)
    search_fields = ('related_user__username',)
    list_filter = ('status',)

    def user_link(self, obj):
        url = reverse('admin:users_customuser_change', args=[obj.related_user_id])
        return format_html(f'<a href="{url}">{obj.related_user}</a>')

    user_link.short_description = 'Пользователь'


models_and_admins = [
    (TaskTypeModel, TaskTypeAdmin),
    (TaskModel, TaskAdmin),
    (TaskModeratorModel, TaskModeratorAdmin),
    (SocialNetworkModel, SocialNetworkAdmin),
    (SocialTaskModel, SocialTaskAdmin),
    (UserTaskModel, UserTaskAdmin),
]

for model, admin_class in models_and_admins:
    admin.site.register(model, admin_class)
