from django.urls import path

from users.views import FribitGetUserViewSet, FribitRedirectUserViewSet

urlpatterns = [
    path('fribit/users/<int:telegram_id>/', FribitGetUserViewSet.as_view({'get': 'get', 'post': 'post', 'patch': 'patch'})),
    path('fribit/redirect/', FribitRedirectUserViewSet.as_view({'get': 'get'})),
]