from django.contrib import admin
from unfold.admin import ModelAdmin

from events.models import Event


@admin.register(Event)
class EventAdmin(ModelAdmin):
    list_filter = ['team', 'active']
    search_fields = ['name', 'indicator']

    fields = [
        'name',
        'date_start', 'date_end',
        'goal',
        ('team', 'active'),
        'telegram_chat',
        'indicator',
        'biscenter'
    ]