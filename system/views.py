from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .serializers import (CollageSerializer, FacultySerializer,
                          LessonSerializer, ScientificGroupSerializer, CreateStudentSerializer,
                          CreateProfessorSerializer, RoomSerializer, CreateRoomSerializer)
from rest_framework.views import APIView
from rest_framework import viewsets, status
from .models import (Collage, Faculty, ScientificGroup,
                     Professor, Student, Room,
                     Lesson, Content, Task, )


class ShowCollagesAPIView(viewsets.ReadOnlyModelViewSet):
    """
        A simple ViewSet for listing and show Collages.
    """
    serializer_class = CollageSerializer
    queryset = Collage.objects.all()


class ShowFacultyAPIView(viewsets.ReadOnlyModelViewSet):
    """
        Another simple ViewSet for listing and showing Faculties.
    """
    serializer_class = FacultySerializer
    queryset = Faculty.objects.all()


class ShowScientificGroupAPIView(viewsets.ReadOnlyModelViewSet):
    """
        Simple ViewSet for listing and showing ScientificGroup.
    """
    serializer_class = ScientificGroupSerializer
    queryset = ScientificGroup.objects.all()


class CreateProfessorAPIView(ListCreateAPIView):
    """
        As the name implies, it is used to create and show a professor
    """
    serializer_class = CreateProfessorSerializer
    queryset = Professor.objects.all()


class CreateStudentAPIView(ListCreateAPIView):
    """
        And this class for showing and creating students
    """
    serializer_class = CreateStudentSerializer
    queryset = Student.objects.all()


class CreateLessonAPIView(ListCreateAPIView):
    """
        Create lesson for Rooms and just staff
        users or professors can create lesson
    """
    permission_classes = (IsAdminUser,)
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class CreateRoomAPIView(CreateAPIView):
    """
        Just staff users (Professors) can create Room
    """
    permission_classes = (IsAdminUser,)
    serializer_class = CreateRoomSerializer
    queryset = Room.objects.all()


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def show_rooms(request):
    """
    List all rooms that student can be there
    """
    if request.method == 'GET':

        try:
            student = Student.objects.get(username=request.user.username)
        except:
            return Response(f'you are not student')
        rooms = Room.objects.filter(status=1, lesson__students__student_number=student.student_number)
        serializer = RoomSerializer(rooms, many=True)

        return Response(serializer.data)


@api_view(['GET'])
def room_detail(request, slug):
    if request.method == 'GET':
        room = Room.objects.filter(slug=slug)
        content = Content.objects.filter(lesson__room=room)
        serializer = RoomSerializer(room, many=True)
        return Response(serializer.data)
