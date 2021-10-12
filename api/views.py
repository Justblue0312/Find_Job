from django.http.response import Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import ProjectSerializer, UserSerializer, StudentSerializer, LectureSerializer
from projects.models import Project
from users.models import User, Student, Lecture
from rest_framework import mixins
from rest_framework import generics


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/users/'},
    ]
    return Response(routes)
