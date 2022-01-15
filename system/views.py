from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from .serializers import (CollageSerializer, FacultySerializer,
                          LessonSerializer, ScientificGroupSerializer, CreateStudentSerializer,
                          CreateProfessorSerializer)
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import (Collage, Faculty, ScientificGroup,
                     Professor, Student, Class,
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
    serializer_class = CreateProfessorSerializer
    queryset = Professor.objects.all()


class CreateStudentAPIView(ListCreateAPIView):
    serializer_class = CreateStudentSerializer
    queryset = Student.objects.all()
