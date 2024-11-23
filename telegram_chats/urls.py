# capitals/urls.py
from django.urls import path
from .views import TelegramChatViewSet

urlpatterns = [
    path('activity/<int:telegram_id>/', TelegramChatViewSet.as_view({'get': 'get'})),
]