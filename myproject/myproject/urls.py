from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),  # Подключаем URL-адреса приложения users
    path('accounts/', include('django.contrib.auth.urls')),  # Добавляем URL-адреса для аутентификации
]
