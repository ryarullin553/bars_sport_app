import os

from celery import Celery
from django.conf import settings
from datetime import timedelta
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('bars_sport_app')
app.config_from_object('django.conf:settings')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'beat_main_task': {
        'task': 'fibit_logs.tasks.main_task',
        'schedule': crontab(hour=23, minute=30),
    },
    'beat_portal_achivments': {
        'task': 'fibit_logs.tasks.portal_achivments',
        'schedule': crontab(hour=1, minute=0, day_of_week=1),
    },
}
