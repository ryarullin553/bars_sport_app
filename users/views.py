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
            return Response(model_to_dict(lst.first()))
        payload = {'user_id': telegram_id, 'login_integrator': INTEGRATOR_LOGIN,
                   'password_integrator': INTEGRATOR_PASSWORD}
        info_user = requests.post('https://test-bo.bars.group/bars_office/telegram_bot/get_employee_info/', data=payload)

        data_user = info_user.json()
        data_user = data_user['extra']
        print(data_user)

        bc, _ = Biscenter.objects.get_or_create(name=data_user['bc'])
        town, _ = Town.objects.get_or_create(name=data_user['town'])
        if data_user:
            lst = User.objects.create(
                name=data_user['full_name'].split(' ')[0],
                surname=data_user['full_name'].split(' ')[1],
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