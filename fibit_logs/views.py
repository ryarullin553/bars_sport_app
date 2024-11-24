import datetime

from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from fibit_logs.models import FibitLog


# Create your views here.
class RatingViewSet(ViewSet):
    http_method_names = ['get']

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
