import uuid

from django.db import models

class Biscenter(models.Model):
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
        db_table = 'biscenters'
        verbose_name = 'Бизнес-центр'
        verbose_name_plural = 'Бизнес-центры'

    def __str__(self):
        return self.name
