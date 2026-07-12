<<<<<<< HEAD
from django.contrib import admin
from django.contrib import admin
from .models import Artwork

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']
# Register your models here.
=======
from django.contrib import admin
from django.contrib import admin
from .models import Artwork

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']
# Register your models here.
>>>>>>> 7956767a86adae2d1e0b7eff85090f4301cedb4a
