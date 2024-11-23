from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from events.models import Event
from users.models import User
from biscenters.models import Biscenter
from telegram_chats.models import TelegramChat
from django.forms import model_to_dict
from django.db.models import Q

from rest_framework.viewsets import ViewSet

class TelegramChatViewSet(ViewSet):
    http_method_names = ['get', 'post', 'head']

    def get(self, request, telegram_id: int, *args, **kwargs):
        user_data = User.objects.filter(telegram_id=telegram_id).first()
        biscenter = user_data.biscenter
        telegramchats = TelegramChat.objects.filter(Q(biscenter=biscenter) | Q(biscenter=None)).values()
        return Response({'post': model_to_dict(telegramchats)})