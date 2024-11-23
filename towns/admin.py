from django.contrib import admin
from unfold.admin import ModelAdmin

from towns.models import Town


@admin.register(Town)
class TownAdmin(ModelAdmin):
    pass