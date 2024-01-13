from django.urls import path
from .views import detail

urlpatterns = [
    path('detail/<int:id>', detail, name='detail')
]