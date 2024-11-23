from django.contrib import admin
from django.urls import path, include

from users.routes import router as user_router
from utils.yasg import urlpatterns as doc_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(user_router.urls)),
    path('api/v1/', include('users.urls')),
    path('', include('activities.urls')),
    path('', include('events.urls')),
    path('', include('telegram_chats.urls'))
]

urlpatterns += doc_api