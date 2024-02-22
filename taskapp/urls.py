from django.urls import path
from . import views 

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('addtask/', views.add_task, name='add_task'),
    path('updatetask/<int:task_id>/', views.update_task, name='update_task'),
    path('tasklist/',views.task_list, name='task_list'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('completed_task/', views.completed_tasks, name='completed_task'),
    path('logout/', views.logout, name='logout'),
]
