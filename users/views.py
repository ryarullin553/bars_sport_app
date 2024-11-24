import datetime

from django.forms import model_to_dict
from django.shortcuts import redirect
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from biscenters.models import Biscenter
from config.settings import INTEGRATOR_LOGIN, INTEGRATOR_PASSWORD, BOT_USERNAME
from towns.models import Town
from users.models import User
from users.serializers import UserSerializer
import requests


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FribitGetUserViewSet(ViewSet):
    http_method_names = ['get', 'post','patch']

    def post(self, request, telegram_id: int):
        post_new = User.objects.filter(telegram_id=telegram_id).update(
            access_token=request.POST['access_token'],
            refresh_token=request.POST['refresh_token'],
            fitbit_user_id=request.POST['user_id'])

        return Response({'count': post_new})

    def patch(self, request, telegram_id: int):
        post_new = User.objects.filter(telegram_id=telegram_id).update(
            code_verifier=request.POST['code_verifier'])
        instance = User.objects.filter(telegram_id=telegram_id).first()
        print(model_to_dict(instance))
        return Response({'count': model_to_dict(instance)})

    def get(self, request, telegram_id: int, *args, **kwargs):
        lst = User.objects.filter(telegram_id=telegram_id)

        if lst:
            user = lst.first()

            user_dict = model_to_dict(user)
            if user.fitbit_user_id:
                activity = get_today_activity(user.access_token, user.fitbit_user_id)
                user_dict['bc'] = user.biscenter.name
                if activity:
                    user_dict['today_activity'] = activity.get('summary').get('steps')
                    user_dict['step_norm_day'] = activity.get('goals').get('steps')
            return Response(user_dict)
        payload = {'user_id': telegram_id, 'login_integrator': INTEGRATOR_LOGIN,
                   'password_integrator': INTEGRATOR_PASSWORD}
        info_user = requests.post('https://test-bo.bars.group/bars_office/telegram_bot/get_employee_info/', data=payload)

        data_user = info_user.json()
        data_user = data_user['extra']
        print(data_user)
        if data_user:
            bc, _ = Biscenter.objects.get_or_create(name=data_user['bc'])
            town, _ = Town.objects.get_or_create(name=data_user['town'])
            lst = User.objects.create(
                username=data_user['username'],
                name=data_user['full_name'].split(' ')[1],
                surname=data_user['full_name'].split(' ')[0],
                patronymic=data_user['full_name'].split(' ')[2],
                biscenter=bc,
                age=data_user['age'],
                sex='Муж' if data_user['pol'] == 0 else 'Жен',
                telegram_id=telegram_id,
                step_norm_day=10000,
                town=town)
            return Response(model_to_dict(lst))
        else:
            return Response({})


class FribitRedirectUserViewSet(ViewSet):
    http_method_names = ['get']
    def get(self, request, *args, **kwargs):

        code = request.GET['code']

        return redirect(f"https:///t.me/{BOT_USERNAME}?start={code}")


def get_today_activity(token, user_id):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    today = datetime.date.today()

    url = f'https://api.fitbit.com/1/user/{user_id}/activities/date/{today.isoformat()}.json'

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None
    else:
        return response.json()