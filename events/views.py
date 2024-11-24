from rest_framework.response import Response
from events.models import Event
from users.models import User
from django.forms import model_to_dict
from django.db.models import Q, Sum, F
from users_in_events.models import UserInEvent
import datetime

from rest_framework.viewsets import ViewSet


class EventsViewSet(ViewSet):
    http_method_names = ['get', 'post', 'patch']

    def get(self, request, telegram_id: int, *args, **kwargs):
        user_data = User.objects.filter(telegram_id=telegram_id).values_list('biscenter', 'id')[0]
        events = Event.objects.exclude(users_in_events__user=user_data[1]).annotate(all_points=Sum('users_in_events__count')).values('id', 'name', 'date_start', 'date_end', 'goal', 'all_points', 'indicator__name')

        return Response({'get': list(events)})

    def post(self, request, telegram_id: int, *args, **kwargs):
        event = Event.objects.get(id=self.request.POST['event_id'])
        user = User.objects.get(telegram_id=telegram_id)
        UserInEvent.objects.create(count=0, user=user, event=event)
        return Response({'post': True})

    def patch(self, request, telegram_id: int, *args, **kwargs):
        user_data = User.objects.filter(telegram_id=telegram_id).values_list('biscenter', 'id')[0]
        events = Event.objects.filter(users_in_events__user=user_data[1]).annotate(all_points=Sum('users_in_events__count')).values('id', 'name', 'date_start', 'date_end', 'goal', 'all_points', 'indicator__name')
        return Response({'patch': list(events)})
