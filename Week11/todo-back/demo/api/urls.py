from django.urls import path, re_path
from api import views

urlpatterns = [
    path('task_lists/', views.task_lists),
    path('task_lists/<int:pk>/', views.task_list_detail),
    path('task_lists/<int:pk>/tasks/', views.task_list_tasks)
]
