from fibit_logs.models import FibitLog
from events.models import Event
from users.models import User
from users_in_events.models import UserInEvent
from indicators.models import Indicator
import datetime
from datetime import timedelta
import requests
from celery import shared_task
from celery_singleton import Singleton
import json

@shared_task(base=Singleton)
def main_task():
    for i in User.objects.exclude(fitbit_user_id=None):
        headers = {
            "Authorization": f"Bearer {i.access_token}",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        today = datetime.date.today()

        indicators = Indicator.objects.all().values_list('id', 'name')

        url = f'https://api.fitbit.com/1/user/{i.fitbit_user_id}/activities/date/{today.isoformat()}.json'

        response = requests.get(url, headers=headers)
        data = response.json()

        for j in indicators:
            FibitLog.objects.create(user_id=i.id, indicator_id=j[0],
                                    count=data.get('summary', {}).get(j[1]))
            for k in UserInEvent.objects.filter(user_id=i.id).filter(
                    event__indicator_id=j[0]).filter(
                    event__date_start__lte=datetime.datetime.now(),
                    event__date_end__gte=datetime.datetime.now()):
                count = k.count + data.get('summary', {}).get(j[1])
                k.update(count=count)

@shared_task(base=Singleton)
def portal_achivments():
    headers = {
        'Content-Type': 'application/json'
    }
    for i in User.objects.exclude(fitbit_user_id=None):
        url = 'https://192.168.227.23/rest/20897/s0b113uk7cgyqeub/fsn_bars.achievement.assign.json'
        today = datetime.datetime.now()
        count = 0
        for k in FibitLog.objects.filter(user_id=i.id, indicator__name='steps', date__gte=today - timedelta(days=7)).values_list('count', flat=True):
            count += k
        if 0 < count/7 <= 5000:
            payload = json.dumps({'USER': i.username,'ACHIEVEMENT': 'TEST_HACKATHON' ,'EXTERNAL_ID': 1})
            requests.request("POST", url, headers=headers, data=payload, verify=False)

        if 5000 < count/7 <= 10000:
            payload = json.dumps({'USER': i.username, 'ACHIEVEMENT': 'TEST_HACKATHON_2', 'EXTERNAL_ID': 2})
            requests.request("POST", url, headers=headers, data=payload, verify=False)

        if count/7 > 10000:
            payload = json.dumps({'USER': i.username, 'ACHIEVEMENT': 'TEST_HACKATHON_3', 'EXTERNAL_ID': 3})
            requests.request("POST", url, headers=headers, data=payload, verify=False)
