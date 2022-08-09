from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TaskSerializer, ProjectSerializer, CommentSerializer
from django.views.decorators.csrf import csrf_exempt

from rest_framework.permissions import IsAuthenticated

from .models import Task, Project, Comment

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
    'List': '/task-list/',
    'Detail View': '/task-details/<str:pk>/',
    'Create': '/task-create/',
    'Update': '/task-update/<str:pk>/',
    'Delete': '/task-delete/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

# CREATE
@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

# READ
@api_view(['GET'])
def taskRead(request, pk):
    serializer = TaskSerializer(data=request.data)
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)

# UPDATE
@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

# DELETE
@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    
    return Response("Deleted Successfully")

"""
PROJECT VIEW
"""

"""
COMMENT VIEW
"""
