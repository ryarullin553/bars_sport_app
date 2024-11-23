import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import UserManager


class User(AbstractBaseUser):
    MALE = 'Муж'
    FEMALE = 'Жен'
    SEX_CHOICES = [
        (MALE, 'Муж'),
        (FEMALE, 'Жен'),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    username = models.CharField(
        max_length=255,
        verbose_name='Логин',
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
    biscenter = models.ForeignKey(
        verbose_name='Бизнес-центр',
        to='biscenters.Biscenter',
        on_delete=models.SET_NULL,
        null=True,
        related_name='users'
    )
    age = models.IntegerField(
        verbose_name='Возраст'
    )
    sex = models.CharField(
        max_length=3,
        choices=SEX_CHOICES,
        verbose_name='Пол'
    )
    step_norm_day = models.IntegerField(
        verbose_name='Норма шагов в день'
    )
    telegram_id = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Телеграм ID'
    )
    town = models.ForeignKey(
        verbose_name='Город',
        to='towns.Town',
        on_delete=models.SET_NULL,
        null=True,
        related_name='users'
    )
    is_block = models.BooleanField(
        verbose_name='Заблокирован',
        default=False
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
    code_verifier = models.TextField(
        verbose_name='Код Фитбита',
        null=True
    )
    access_token = models.TextField(
        verbose_name='access token',
        null=True
    )
    refresh_token = models.TextField(
        verbose_name='refresh token',
        null=True
    )
    fitbit_user_id = models.TextField(
        verbose_name='ID пользователя Фитбит',
        null=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.name
