from django.urls import path
from .views import ShowCollagesAPIView, ShowFacultyAPIView, CreateStudentAPIView, CreateProfessorAPIView, \
    CreateLessonAPIView

urlpatterns = [
    path('collages/', ShowCollagesAPIView.as_view({'get': 'list'})),
    path('faculties/', ShowFacultyAPIView.as_view({'get': 'list'})),
    path('signup/student/', CreateStudentAPIView.as_view()),
    path('signup/professor/', CreateProfessorAPIView.as_view()),
    path('create/class/', CreateLessonAPIView.as_view()),
]
