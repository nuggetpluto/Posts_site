from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from django.contrib.auth.views import LogoutView


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Измените на имя вашего главного представления
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    # Логика входа пользователя
    return render(request, 'users/login.html')


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # Получение всех постов
    return render(request, 'users/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'users/post_detail.html', {'post': post})


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')

    else:
        form = PostForm()
    return render(request, 'users/post_form.html', {'form': form})


def home(request):
    return render(request, 'users/home.html')  # Создадим шаблон home.html


@login_required  # Ограничиваем доступ только для авторизованных пользователей
def profile(request):
    return render(request, 'users/profile.html', {'user': request.user})


class CustomLogoutView(LogoutView):
    template_name = 'users/logged_out.html'

