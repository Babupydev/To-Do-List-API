from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),        # To list and create tasks
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),  # To retrieve, update, or delete tasks
]