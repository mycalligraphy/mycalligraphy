<<<<<<< HEAD
from django.contrib import admin
from django.contrib import admin
from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'artwork', 'text', 'created_at', 'is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['user__username', 'artwork__title', 'text']

=======
from django.contrib import admin
from django.contrib import admin
from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'artwork', 'text', 'created_at', 'is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['user__username', 'artwork__title', 'text']

>>>>>>> 7956767a86adae2d1e0b7eff85090f4301cedb4a
