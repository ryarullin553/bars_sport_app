import uuid

from django.db import models


class TelegramChat(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=255
    )
    chat_id = models.CharField(
        verbose_name='ID чата в Telegram',
        max_length=255
    )

    class Meta:
        db_table = 'telegram_chat'
        verbose_name = 'Чат в Telegram'
        verbose_name_plural = 'Чаты в Telegram'

    def __str__(self):
        return self.name
