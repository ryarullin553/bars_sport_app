import uuid

from django.db import models

class Indicator(models.Model):
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

    class Meta:
        db_table = 'indicator'
        verbose_name = 'Индикатор'
        verbose_name_plural = 'Индикаторы'

    def __str__(self):
        return self.name
