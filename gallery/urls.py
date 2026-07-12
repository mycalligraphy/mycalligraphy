<<<<<<< HEAD



from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.gallery_view, name='gallery_list'),
    path('like/<int:artwork_id>/', views.like_artwork, name='like_artwork'),
    path('view/<int:artwork_id>/', views.view_artwork, name='view_artwork'),
=======



from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.gallery_view, name='gallery_list'),
    path('like/<int:artwork_id>/', views.like_artwork, name='like_artwork'),
    path('view/<int:artwork_id>/', views.view_artwork, name='view_artwork'),
>>>>>>> 7956767a86adae2d1e0b7eff85090f4301cedb4a
]