from django.urls import path
from .views import register, login_view
from .views import post_list, post_detail, post_create
from .views import home, profile, like_post, edit_profile
from django.contrib.auth import views as auth_views
from .views import CustomLogoutView

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('posts/', post_list, name='post_list'),
    path('posts/<int:pk>/', post_detail, name='post_detail'),
    path('posts/new/', post_create, name='post_create'),
    path('accounts/profile/', profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('posts/<int:pk>/like/', like_post, name='like_post'),
    path('profile/edit/', edit_profile, name='edit_profile'),
]