from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FibitLogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fibit_logs'
    verbose_name = _('Логи Fibit')
