import datetime

from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from fibit_logs.models import FibitLog
from fibit_logs.tasks import main_task, portal_achivments


# Create your views here.
class RatingViewSet(ViewSet):
    http_method_names = ['get', 'post', 'path']

    def get(self, request, telegram_id: int, *args, **kwargs):
        query = FibitLog.objects. \
        filter(
            date__gte=datetime.datetime.now() - datetime.timedelta(days=1),
            date__lt=datetime.datetime.now(),
            indicator__name='steps',
        ) \
            .order_by('-count') \
            .values_list('count', 'date', 'user__name', 'user__surname',
                         'user__biscenter__name')
        rating = list(query)
        return Response({'rating': rating})

    def post(self, request, telegram_id: int, *args, **kwargs):
        main_task()
        return Response({})

    def path(self, request, telegram_id: int, *args, **kwargs):
        portal_achivments()
        return Response({})