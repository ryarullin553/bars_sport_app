from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TelegramChatsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'telegram_chats'
    verbose_name = _('Чаты в Telegram')
