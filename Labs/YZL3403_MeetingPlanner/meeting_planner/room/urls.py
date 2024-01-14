from django.urls import path
from .views import room_list, detail

urlpatterns = [
    path('list', room_list, name='room_list'),
    path('detail/<int:id>', detail, name='detail'),
]