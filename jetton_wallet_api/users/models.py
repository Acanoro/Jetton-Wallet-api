from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class AvatarsModel(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название каталога')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')
    link = models.URLField(verbose_name='Ссылка н аватарку')
    active = models.BooleanField(default=True, verbose_name='доступ')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Аватарка'
        verbose_name_plural = 'Аватарка'


class LanguagesModel(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Язык')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')
    iso_code = models.CharField(max_length=10, unique=True, verbose_name='iso_code')
    active = models.BooleanField(default=True, verbose_name='доступ')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Язык'


class CustomUser(AbstractUser):
    related_avatar = models.ForeignKey(
        AvatarsModel,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Аватарка"
    )
    related_languages = models.ForeignKey(
        LanguagesModel,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Язык"
    )

    telegram_id = models.IntegerField(unique=True, verbose_name='Telegram ID', null=True, blank=True, )
    balance = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name='Баланс'
    )
    twitter_account = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Twitter аккаунт"
    )
    youtube_account = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="YouTube аккаунт"
    )
    remaining_invites = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        verbose_name='Оставшиеся приглашения'
    )

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователь'


class ModeratorsModel(models.Model):
    related_user = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Пользователь'
    )

    def __str__(self):
        return f'{self.related_user.name}'

    class Meta:
        verbose_name = 'Модераторы'
        verbose_name_plural = 'Модераторы'


class NameWalletModel(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название кошелька")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Название кошелька'
        verbose_name_plural = 'Название кошелька'


class TonWalletModel(models.Model):
    related_name_wallet = models.ForeignKey(
        NameWalletModel,
        on_delete=models.SET_NULL,
        null=True,
        related_name='nameWallets',
    )
    related_user = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Пользователь',
        related_name='wallets'
    )

    date = models.DateTimeField(verbose_name='Дата добавления')

    def __str__(self):
        return f'TonWalletObject'

    class Meta:
        verbose_name = 'TonWallet'
        verbose_name_plural = 'TonWallet'


class ReferralsModel(models.Model):
    related_user = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Пользователь',
        related_name='user_referrals'
    )

    related_user_referral = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Пользователь реферал',
        related_name='referrals'
    )

    timestamp = models.DateTimeField(verbose_name='Дата добавления')
    reward_amount = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name='Сумма бонуса'
    )

    def __str__(self):
        return f'TonWalletObject'

    class Meta:
        verbose_name = 'TonWallet'
        verbose_name_plural = 'TonWallet'
