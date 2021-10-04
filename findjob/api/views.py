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

"""
 Get all apis
 """


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/users/'},

        {'GET': '/api/projects/'},
        {'GET': '/api/projects/id'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
    ]
    return Response(routes)


@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def updateProject(request, pk):
    # try:
    #     project = Project.objects.get(id=pk)
    # except Project.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    project = Project.objects.get(id=pk)
    if request.method == 'PUT':
        serializer = ProjectSerializer(project, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["sucess"] = 'update successfully'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getProject(request, pk):
    try:
        project = Project.objects.get(id=pk)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProjectSerializer(project, many=False)
        return Response(serializer.data)


@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getUser(request, pk):
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)


@api_view(['GET'])
def getStudents(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getStudent(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getLectures(request):
    lectures = Lecture.objects.all()
    serializer = LectureSerializer(lectures, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getLecture(request, pk):
    lecture = Lecture.objects.get(id=pk)
    serializer = LectureSerializer(lecture, many=False)
    return Response(serializer.data)
