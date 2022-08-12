from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TicketSerializer, ProjectSerializer, CommentSerializer
from django.views.decorators.csrf import csrf_exempt

from rest_framework.permissions import IsAuthenticated

from .models import Ticket, Project, Comment


'''
https://api/v1/dashboard/
https://api/v1/project/{project_id}/
https://api/v1/project/{project_id}/ticket/all/
https://api/v1/project/{project_id}/ticket/{ticket_id}/comment/all/
https://api/v1/project/{project_id}/ticket/{ticket_id}/comment/{comment_id}/
'''

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
def ticketList(request):
    tickets = Ticket.objects.all()
    serializer = TicketSerializer(tickets, many=True)
    return Response(serializer.data)

# CREATE
@api_view(['POST'])
def ticketCreate(request):
	serializer = TicketSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

# READ
@api_view(['GET'])
def ticketRead(request, pk):
    serializer = TicketSerializer(data=request.data)
    ticket = Ticket.objects.get(id=pk)
    serializer = TicketSerializer(ticket, many=False)
    return Response(serializer.data)

# UPDATE
@api_view(['POST'])
def ticketUpdate(request, pk):
    ticket = Ticket.objects.get(id=pk)
    serializer = TicketSerializer(instance=ticket, data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

# DELETE
@api_view(['DELETE'])
def ticketDelete(request, pk):
    ticket = Ticket.objects.get(id=pk)
    ticket.delete()
    
    return Response("Deleted Successfully")

# GET Tickets by foreign key "projectID"
# New ticket list will be similar to this
@api_view(['GET'])
def ticketListByProjectID(request, fk):
    project = Project.objects.get(id=fk)
    tickets = project.projectID.all()
    serializer = TicketSerializer(tickets, many=True)
    return Response(serializer.data)
    

"""
PROJECT VIEW
"""

    
# Projects list will be displayed on teh dashboard page 
@api_view(['GET'])
def projectList(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


# CREATE
@api_view(['POST'])
def projectCreate(request):
	serializer = ProjectSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

# READ
@api_view(['GET'])
def projectRead(request, pk):
    serializer = ProjectSerializer(data=request.data)
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)

# UPDATE
@api_view(['POST'])
def projectUpdate(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(instance=project, data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

# DELETE
@api_view(['DELETE'])
def projectDelete(request, pk):
    project = Project.objects.get(id=pk)
    project.delete()
    
    return Response("Deleted Successfully")

"""
COMMENT VIEW
"""

@api_view(['GET'])
def commentListAll(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

# GET Comment by foreign key "ticketID"
# New ticket list will be similar to this
@api_view(['GET'])
def commentList(request, fk):
    ticket = Ticket.objects.get(id=fk)
    print(ticket)
    comments = ticket.ticketID.all()
    print(comments)
    print()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

# CREATE
@api_view(['POST'])
def commentCreate(request):
	serializer = CommentSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

# READ
@api_view(['GET'])
def commentRead(request, pk):
    serializer = CommentSerializer(data=request.data)
    comment = Comment.objects.get(id=pk)
    serializer = CommentSerializer(comment, many=False)
    return Response(serializer.data)

# UPDATE
@api_view(['POST'])
def commentUpdate(request, pk):
    comment = Comment.objects.get(id=pk)
    serializer = CommentSerializer(instance=comment, data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

# DELETE
@api_view(['DELETE'])
def commentDelete(request, pk):
    comment = Comment.objects.get(id=pk)
    comment.delete()
    
    return Response("Deleted Successfully")
