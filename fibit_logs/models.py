import uuid

from django.db import models

class FibitLog(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    indicator = models.ForeignKey(
        verbose_name='Индикатор',
        to='indicators.Indicator',
        on_delete=models.CASCADE,
        related_name='fibit_logs'
    )
    date = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата'
    )
    count = models.IntegerField(
        verbose_name='Количество'
    )
    user = models.ForeignKey(
        verbose_name='Пользователь',
        to='users.User',
        on_delete=models.CASCADE,
        related_name='fibit_logs'
    )

    class Meta:
        db_table = 'fibit_log'
        verbose_name = 'Лог Fibit'
        verbose_name_plural = 'Логи Fibit'


