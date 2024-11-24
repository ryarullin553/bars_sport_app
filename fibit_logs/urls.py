from django.urls import path
from .views import RatingViewSet




urlpatterns = [
    path('rating/<int:telegram_id>/', RatingViewSet.as_view({'get': 'get', 'post': 'post', 'path': 'path'})),
]
