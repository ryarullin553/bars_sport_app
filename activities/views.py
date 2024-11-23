from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse

from activities.models import Activity
from events.models import Event
from users.models import User
from biscenters.models import Biscenter
from django.forms import model_to_dict
import datetime
from django.db.models import Q, Count, F

from rest_framework.viewsets import ViewSet


class ActivityViewSet(ViewSet):
    http_method_names = ['get', 'post', 'patch']

    def get(self, request, telegram_id: int, *args, **kwargs):
        user_data = User.objects.filter(telegram_id=telegram_id).values_list('biscenter', 'id', 'town')[0]
 #.filter(Q(biscenter=user_data[0]) | Q(biscenter=None))
        activity = Activity.objects.exclude(user=user_data[1]).filter(date_start__gte=datetime.date.today()).filter(
            Q(town=user_data[2]) | Q(town_filter=None)).annotate(user_count=Count('user')).filter(users_max_count__gte=F('user_count')).values('id', 'name', 'town', 'date_start', 'user_count', 'users_max_count')
        return Response({'get': list(activity)})

    def post(self, request, telegram_id: int, *args, **kwargs):
        activity = Activity.objects.get(id=self.request.POST['activity_id'])
        user = User.objects.get(telegram_id=telegram_id)
        activity.user.add(user)
        activity.save()
        return Response({'post': model_to_dict(activity)})

    def patch(self, request, telegram_id: int, *args, **kwargs):
        user_data = User.objects.filter(telegram_id=telegram_id).values_list('biscenter', 'id', 'town')[0]
        activity = Activity.objects.filter(user=user_data[1]).filter(date_start__gte=datetime.date.today()).values('id', 'name', 'town', 'date_start')
        return Response({'patch': list(activity)})

