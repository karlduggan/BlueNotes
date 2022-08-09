from django.contrib import admin
from django.urls import path, include
from . import views
"""
Need completing for comments and projects
- Get all commment from a ticket
- Get all tickets from a project 
"""
urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    # Project CRUD
    path('project-list/', views.projectList, name='project-list'),
    path('project-create/', views.projectCreate, name="project-create"),
    path('project-read/<str:pk>/', views.projectRead, name='project-read'),
    path('project-update/<str:pk>/', views.projectUpdate, name="project-update"),
    path('project-delete/<str:pk>/', views.projectDelete, name="project-delete"),
    # Tasks / Tickets CRUD
    path('task-list/', views.taskList, name='task-list'),
    path('task-create/', views.taskCreate, name="task-create"),
    path('task-read/<str:pk>/', views.taskRead, name='task-read'),
    path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
    path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
    # Comments CRUD 
    path('comment-list/', views.commentList, name='comment-list'),
    path('comment-create/', views.commentCreate, name="comment-create"),
    path('comment-read/<str:pk>/', views.commentRead, name='comment-read'),
    path('comment-update/<str:pk>/', views.commentUpdate, name="comment-update"),
    path('comment-delete/<str:pk>/', views.commentDelete, name="comment-delete"),
]