from models import FibitLog
from events.models import Event
from users.models import User
from users_in_events.models import UserInEvent
import datetime
import requests

def main_task():
    for i in Event.objects.all():
        s = 0
        for i in UserInEvent.objects.filter(event=i):
            s += i.count
        if (i.date_start < datetime.date.today() < i.date_end) and (s < i.goal):
            i.active = True
        else:
            i.active = False
    for i in User.objects.exclude(fitbit_user_id=None):
        headers = {
            "Authorization": f"Bearer {i.access_token}",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        today = datetime.date.today()

        indicators = ['step', 'cal']
        url = f'https://api.fitbit.com/1/user/{i.fitbit_user_id}/activities/date/{today.isoformat()}.json'

        response = requests.get(url, headers=headers)
        data = response.json()

        for j in indicators:
            FibitLog.objects.create(user_id=i.id,indicator_id=j,count=getattr(data.get('summary'), j))
            for k in UserInEvent.objects.filter(user_id=i.id, event__active=True):
                k.update(count=getattr(data.get('summary'), j))