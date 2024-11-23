import uuid

from django.db import models

class UserInEvent(models.Model):
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
    count = models.IntegerField(
        verbose_name='Количество'
    )
    user = models.ForeignKey(
        verbose_name='Пользователь',
        to='users.User',
        on_delete=models.CASCADE,
        related_name='users_in_events'
    )
    event = models.ForeignKey(
        verbose_name='Командная активность',
        to='events.Event',
        on_delete=models.SET_NULL,
        null=True,
        related_name='users_in_events'
    )

    class Meta:
        db_table = 'user_in_event'
        verbose_name = 'Участники активности'
        verbose_name_plural = 'Участники активности'

    def __str__(self):
        return self.name
