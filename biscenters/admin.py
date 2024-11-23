from django.contrib import admin
from unfold.admin import ModelAdmin

from biscenters.models import Biscenter


@admin.register(Biscenter)
class BiscenterAdmin(ModelAdmin):
    pass