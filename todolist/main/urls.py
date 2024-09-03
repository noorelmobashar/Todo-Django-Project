from django.urls import path
from .views import index, show_tasks, show_details, show_tasks_by_status, register, login, logout, create_category, create_task, update_category, delete_category, update_task, delete_task
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect

urlpatterns = [
    path('', index, name='index'),
    path('tasks/<name>', show_tasks, name="tasks"),
    path('tasks/<catid>/details/<id>', show_details , name="details"),
    path('<status>', show_tasks_by_status, name="tasks_by_status"),
    path('accounts/register', register, name='register'),
    path('accounts/login', login, name='login'),
    path('accounts/logout', logout, name='logout'),
    path('create/category', create_category, name='createcat'),
    path('create/task', create_task, name='createtask'),
    path('update/category/<id>', update_category, name='updatecat'),
    path('delete/category/<id>', delete_category, name='deletecat'),
    path('update/<cat>/<id>', update_task, name='updatetask'),
    path('delete/<cat>/<id>', delete_task, name='deletetask'),
]
