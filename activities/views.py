from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse

from activities.models import Activity
from events.models import Event
from users.models import User
from biscenters.models import Biscenter
from django.forms import model_to_dict
import datetime
from django.db.models import Q

from rest_framework.viewsets import ViewSet

class ActivityViewSet(ViewSet):
    http_method_names = ['get', 'post', 'head']

    def get(self, request, telegram_id: int, *args, **kwargs):
        user_data = User.objects.filter(telegram_id=telegram_id).values_list('biscenter','id','town')[0]
        activity = Activity.objects.exlude(user=user_data[1]).filter(date_start__gte=datetime.date.today()).filter(Q(biscenter=user_data[0]) | Q(biscenter=None)).values().filter(Q(town=user_data[2]) | Q(town_filter=None)).values()
        return Response({'post': model_to_dict(activity)})