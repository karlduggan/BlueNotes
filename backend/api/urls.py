from django.contrib import admin
from django.urls import path, include
from . import views
"""
Need completing for comments and projects
- Get all commment from a ticket
- Get all tickets from a project 

pk = primary key
<int:pk>
<str:pk>
"""
urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    # Project CRUD
    path('project-list/', views.projectList, name='project-list'),
    path('project-create/', views.projectCreate, name="project-create"),
    path('project-read/<str:pk>/', views.projectRead, name='project-read'),
    path('project-update/<str:pk>/', views.projectUpdate, name="project-update"),
    path('project-delete/<str:pk>/', views.projectDelete, name="project-delete"),
    # Tickets CRUD
    path('ticket-list/', views.ticketList, name='ticket-list'),
    path('ticket-list-by-project-id/<str:fk>/', views.ticketListByProjectID, name="ticket-list-by-project-id"),
    path('ticket-create/', views.ticketCreate, name="ticket-create"),
    path('ticket-read/<str:pk>/', views.ticketRead, name='ticket-read'),
    path('ticket-update/<str:pk>/', views.ticketUpdate, name="ticket-update"),
    path('ticket-delete/<str:pk>/', views.ticketDelete, name="ticket-delete"),
    # Comments CRUD 
    path('comment-list-all/', views.commentListAll, name='comment-list-all'),
    path('comment-list/<str:fk>', views.commentList, name='comment-list'),
    path('comment-create/', views.commentCreate, name="comment-create"),
    path('comment-read/<str:pk>/', views.commentRead, name='comment-read'),
    path('comment-update/<str:pk>/', views.commentUpdate, name="comment-update"),
    path('comment-delete/<str:pk>/', views.commentDelete, name="comment-delete"),
]