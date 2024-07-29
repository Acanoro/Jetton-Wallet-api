from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from users.models import *


# Register your models here.
class AvatarsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'active',)
    search_fields = ('name',)
    list_filter = ('active',)


class LanguagesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'active',)
    search_fields = ('name',)
    list_filter = ('active',)


class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'username',
        'telegram_id',
        'balance',
        'twitter_account',
        'youtube_account',
        'remaining_invites'
    )
    search_fields = ('username', 'telegram_id',)
    list_filter = ('remaining_invites',)


class ModeratorsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user_link',)
    search_fields = ('related_user__username',)

    def user_link(self, obj):
        url = reverse('admin:users_customuser_change', args=[obj.related_user_id])
        return format_html(f'<a href="{url}">{obj.related_user}</a>')

    user_link.short_description = 'Пользователь'


class NameWalletAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    search_fields = ('name',)


class TonWalletAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user_link', 'date',)
    search_fields = ('related_user__username',)

    def user_link(self, obj):
        url = reverse('admin:users_customuser_change', args=[obj.related_user_id])
        return format_html(f'<a href="{url}">{obj.related_user}</a>')

    user_link.short_description = 'Пользователь'


class ReferralsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user_link', 'user_link_referral',)
    search_fields = ('related_user__username', 'related_user_referral__username')

    def user_link_referral(self, obj):
        url = reverse('admin:users_customuser_change', args=[obj.related_user_id])
        return format_html(f'<a href="{url}">{obj.related_user}</a>')

    user_link_referral.short_description = 'Пользователь'

    def user_link(self, obj):
        url = reverse('admin:users_customuser_change', args=[obj.related_user_id])
        return format_html(f'<a href="{url}">{obj.related_user}</a>')

    user_link.short_description = 'Пользователь реферал'


models_and_admins = [
    (AvatarsModel, AvatarsAdmin),
    (LanguagesModel, LanguagesAdmin),
    (CustomUser, CustomUserAdmin),
    (ModeratorsModel, ModeratorsAdmin),
    (NameWalletModel, NameWalletAdmin),
    (TonWalletModel, TonWalletAdmin),
    (ReferralsModel, ReferralsAdmin),
]

for model, admin_class in models_and_admins:
    admin.site.register(model, admin_class)
