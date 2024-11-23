import uuid

from django.db import models

class Activity(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    town = models.ForeignKey(
        verbose_name='Город',
        to='towns.Town',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='activities'
    )
    town_filter = models.BooleanField(
        verbose_name="Ограничение по городу"
    )
    date_start = models.DateTimeField(
        verbose_name='Дата начала'
    )
    users_count = models.IntegerField(
        verbose_name='Количество участников',
        default=0,
        null=True,
        blank=True
    )
    users_max_count = models.IntegerField(
        verbose_name='Максимальное количество участников',
        null=True,
        blank=True
    )
    telegram_chat = models.ForeignKey(
        verbose_name='Чат в Telegram',
        to='telegram_chats.TelegramChat',
        on_delete=models.SET_NULL,
        related_name='activities',
        null=True,
        blank=True
    )
    user = models.ManyToManyField(
        verbose_name='Пользователь',
        to='users.User',
        related_name='activities',
        null=True,
        blank=True
    )
    biscenter = models.ManyToManyField(
        verbose_name='Бизнес-центр',
        to='biscenters.Biscenter',
        related_name='activities',
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'activity'
        verbose_name = 'Тренировки'
        verbose_name_plural = 'Тренировки'


    def __str__(self):
        return self.name