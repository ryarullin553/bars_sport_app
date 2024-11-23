from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from fibit_logs.models import FibitLog
from users.models import User
import datetime


# Create your views here.
class RatingViewSet(ViewSet):
    http_method_names = ['get']

    def get(self, request, telegram_id: int, *args, **kwargs):
        rating = list(FibitLog.objects.filter(
            date__gte=datetime.datetime.now() - datetime.timedelta(days=1),
            date__lt=datetime.datetime.now(),
            indicator__name='Шаги',
        ).order_by('-count').values_list())

        my_activity = list(FibitLog.objects.filter(
            date__gte=datetime.datetime.now() - datetime.timedelta(days=1),
            date__lt=datetime.datetime.now(),
            indicator__name='Шаги',
            user__telegram_id=telegram_id,
        ).order_by('-count').values_list(flat=True))

        position = rating.index(my_activity)

        rendered_rating = []

        for i, rate in enumerate(rating[:5]):
            rendered_rating.append([i + 1] + rate)

        rendered_rating.append([position + 1] + my_activity)

        return Response({'rating': rendered_rating})
