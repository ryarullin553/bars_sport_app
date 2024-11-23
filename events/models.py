import uuid

from django.db import models

class Event(models.Model):
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
    date_start = models.DateTimeField(
        verbose_name='Дата начала'
    )
    date_end = models.DateTimeField(
        verbose_name='Дата окончания'
    )
    goal = models.IntegerField(
        verbose_name='Цель'
    )
    points = models.IntegerField(
        verbose_name='Очки'
    )
    team = models.BooleanField(
        verbose_name='Командное событие'
    )
    telegram_chat = models.ForeignKey(
        verbose_name='Чат в Telegram',
        to='telegram_chats.TelegramChat',
        on_delete=models.SET_NULL,
        null=True,
        related_name='events'
    )
    indicator = models.ForeignKey(
        verbose_name='Индикатор',
        to='indicators.Indicator',
        on_delete=models.SET_NULL,
        null=True,
        related_name='events'
    )
    biscenter = models.ManyToManyField(
        verbose_name='Бизнес-центр',
        to='biscenters.Biscenter',
        related_name='events',
        null=True
    )

    class Meta:
        db_table = 'event'
        verbose_name = 'Командная активность'
        verbose_name_plural = 'Командные активности'

    def __str__(self):
        return self.name