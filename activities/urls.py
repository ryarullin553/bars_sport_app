# capitals/urls.py
from django.urls import path
from .views import ActivityViewSet

urlpatterns = [
    path('activity/<int:telegram_id>/', ActivityViewSet.as_view({'get': 'get'})),
]