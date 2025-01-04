# birthday/urls.py
from django.urls import path

from . import views

app_name = 'birthday'

urlpatterns = [
    path('', views.birthday, name='create'),
    # Новый маршрут.
    path('list/', views.birthday_list, name='list')
]