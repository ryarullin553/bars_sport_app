import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import UserManager


class User(AbstractBaseUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    name = models.TextField(
        verbose_name='Имя'
    )
    surname = models.TextField(
        verbose_name='Фамилия'
    )
    patronymic = models.TextField(
        verbose_name='Отчество'
    )
    biscenter = models.TextField(
        verbose_name='Бизнес-центр'
    )
    age = models.TextField(
        verbose_name='Возраст'
    )
    sex = models.BooleanField(
        verbose_name='Пол'
    )
    step_norm_day = models.IntegerField(
        verbose_name='Норма шагов в день'
    )
    procent_day = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='Процент дня'
    )
    telegram_id = models.IntegerField(
        unique=True,
        verbose_name='Телеграм ID'
    )
    town = models.CharField(
        max_length=255,
        verbose_name='Город'
    )
    block = models.BooleanField(
        verbose_name='Блокировка'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активен'
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name='Персонал'
    )
    is_superuser = models.BooleanField(
        default=False,
        verbose_name='Суперпользователь'
    )

    objects = UserManager()

    USERNAME_FIELD = 'telegram_id'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.name
