import uuid

from django.db import models

class Town(models.Model):
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
        db_table = 'town'
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name