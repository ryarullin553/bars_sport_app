from django.contrib import admin
from unfold.admin import ModelAdmin

from users.models import User


@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ['surname', 'name', 'patronymic', 'biscenter']
    # list_display_links = ('id', 'title')
    list_filter = ['biscenter', 'town']
    search_fields = ['username', 'age']

    fields = [
        'username',
        ('name', 'surname', 'patronymic'),
        'biscenter',
        'age',
        'sex',
        'telegram_id',
        'town',
        'is_active',
        'is_staff',
        'is_superuser'
    ]