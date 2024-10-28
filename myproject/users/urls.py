from django.urls import path
from .views import register, login_view
from .views import post_list, post_detail
from .views import post_create
from .views import home
from .views import profile
from django.contrib.auth import views as auth_views
from .views import CustomLogoutView

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('posts/', post_list, name='post_list'),  # Список постов
    path('posts/<int:pk>/', post_detail, name='post_detail'),  # Детали поста
    path('posts/new/', post_create, name='post_create'),  # Создание нового поста
    path('accounts/profile/', profile, name='profile'),  # URL для личного кабинета
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # URL для выхода
]
