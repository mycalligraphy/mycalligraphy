<<<<<<< HEAD
from django.urls import path
from . import views

app_name = 'comments'

urlpatterns = [
    path('add/<int:artwork_id>/', views.add_comment, name='add_comment'),
=======
from django.urls import path
from . import views

app_name = 'comments'

urlpatterns = [
    path('add/<int:artwork_id>/', views.add_comment, name='add_comment'),
>>>>>>> 7956767a86adae2d1e0b7eff85090f4301cedb4a
]