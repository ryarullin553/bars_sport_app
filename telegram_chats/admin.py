from django.contrib import admin
from unfold.admin import ModelAdmin

from telegram_chats.models import TelegramChat


@admin.register(TelegramChat)
class TelegramChatAdmin(ModelAdmin):
    pass