from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_rickmorty_data_view, name='home'),
]
