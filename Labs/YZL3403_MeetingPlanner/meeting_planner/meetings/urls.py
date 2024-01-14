from django.urls import path
from .views import detail, create, update, delete

urlpatterns = [
    path('detail/<int:id>', detail, name='detail'),
    path('create', create, name='create'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
]