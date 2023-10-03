from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('load/', views.get_rickmorty_data_view, name='load'),
    path('save-rick/', views.rick_game, name='game'),
]
