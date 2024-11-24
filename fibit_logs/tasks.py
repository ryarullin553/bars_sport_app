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
    for i in User.objects.exclude(fitbit_user_id=None):
        today = datetime.datetime.now()
        count = 0
        for i in FibitLog.objects.filter(user_id=i.id, indicator__name='steps', date_gte=today - timedelta(days=7)).values_list('count', flat=True):
            count += i
        if 0 <= count <= 5000:
            payload = {'USER': i.username,'ACHIEVEMENT': 'TEST_HACKATHON' ,'EXTERNAL_ID': 1}
            requests.post('https://192.168.227.23/rest/20897/s0b113uk7cgyqeub/fsn_bars.achievement.assign.json',data=payload)

        if 5000 < count <= 10000:
            payload = {'USER': i.username, 'ACHIEVEMENT': 'TEST_HACKATHON2', 'EXTERNAL_ID': 2}
            requests.post('https://192.168.227.23/rest/20897/s0b113uk7cgyqeub/fsn_bars.achievement.assign.json',
                          data=payload)

        if count > 10000:
            payload = {'USER': i.username, 'ACHIEVEMENT': 'TEST_HACKATHON3', 'EXTERNAL_ID': 3}
            requests.post('https://192.168.227.23/rest/20897/s0b113u7cgyqeub/fsn_bars.achievement.assign.json',
                          data=payload)
