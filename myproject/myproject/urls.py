from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),  # Подключаем URL-адреса приложения users
    path('accounts/', include('django.contrib.auth.urls')),  # Добавляем URL-адреса для аутентификации
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)