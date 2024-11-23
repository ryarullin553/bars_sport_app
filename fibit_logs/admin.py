from django.contrib import admin
from unfold.admin import ModelAdmin

from fibit_logs.models import FibitLog


@admin.register(FibitLog)
class FibitLogAdmin(ModelAdmin):
    pass