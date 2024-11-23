from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class TownsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'towns'
    verbose_name = _('Города')
