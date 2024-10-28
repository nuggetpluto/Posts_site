from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')  # Отображение полей в списке
    list_filter = ('author',)  # Фильтрация по автору
    search_fields = ('title', 'content')  # Поиск по заголовку и содержимому
