from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import routers, serializers, viewsets

import json

# Create your views here.

def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type="text/json")

def foo(request):
    response = json.dumps([{'test': 909090}])
    return HttpResponse(response, content_type="text/json")