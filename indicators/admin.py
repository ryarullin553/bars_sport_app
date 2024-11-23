from django.contrib import admin
from unfold.admin import ModelAdmin

from indicators.models import Indicator


@admin.register(Indicator)
class IndicatorAdmin(ModelAdmin):
    pass