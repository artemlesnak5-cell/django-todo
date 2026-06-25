# todo_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('/tasks/')),  # Перенаправление на задачи
    path('users/', include('users.urls')),
    path('tasks/', include('tasks.urls')),
]