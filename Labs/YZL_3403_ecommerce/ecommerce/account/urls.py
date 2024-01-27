from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('my_login/', views.my_login, name='my_login'),
    path('user-logout/', views.user_logout, name='user_logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile_management/', views.profile_management, name='profile-management'),
    path('delete-account/', views.delete_account, name='delete-account'),
]


