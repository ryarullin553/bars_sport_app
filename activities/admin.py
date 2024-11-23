from django.contrib import admin
from unfold.admin import ModelAdmin

from activities.models import Activity


@admin.register(Activity)
class ActivityAdmin(ModelAdmin):
    list_filter = ['town_filter']
    search_fields = ['name', 'biscenter']

    fields = [
        'name',
        'date_start',
        'town_filter',
        'town',
        ('users_count', 'users_max_count'),
        'telegram_chat',
        'biscenter',
        'user'
    ]