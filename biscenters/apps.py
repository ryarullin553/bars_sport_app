from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BiscentersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'biscenters'
    verbose_name = _('Бизнес-центры')
