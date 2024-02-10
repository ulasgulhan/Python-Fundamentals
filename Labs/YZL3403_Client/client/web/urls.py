from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_categories, name='categories'),
    path('category/<int:id>', views.get_categories_by_id, name='detail'),
    path('category/create', views.create_category, name='create'),
    path('category/update/<int:id>', views.update_category, name='update'),
    path('category/delete/<int:id>', views.delete_category, name='delete'),
]