# capitals/urls.py
from django.urls import path
from .views import EventsViewSet

urlpatterns = [
    path('events/<int:telegram_id>/', EventsViewSet.as_view({'get': 'get'})),
]