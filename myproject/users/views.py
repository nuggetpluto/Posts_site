from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Like, UserProfile
from .forms import PostForm, CustomUserCreationForm, CommentForm, UserProfileForm
from django.contrib.auth.views import LogoutView
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Ваш аккаунт был создан, {email}! Теперь вы можете войти.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    return render(request, 'users/login.html')


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'users/post_list.html', {'posts': posts})


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'users/post_detail.html', context)


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
    return render(request, 'users/home.html')


@login_required
def profile(request):
    return render(request, 'users/profile.html', {'user': request.user})


class CustomLogoutView(LogoutView):
    template_name = 'users/logged_out.html'


@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        like.delete()

    # Возвращаем пользователя обратно на страницу, с которой был сделан запрос
    return redirect(request.META.get('HTTP_REFERER', 'post_list'))


@login_required
def edit_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'users/edit_profile.html', {'form': form})
