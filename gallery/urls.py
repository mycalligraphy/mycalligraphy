


from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.gallery_view, name='gallery_list'),
    path('like/<int:artwork_id>/', views.like_artwork, name='like_artwork'),
    path('view/<int:artwork_id>/', views.view_artwork, name='view_artwork'),
]