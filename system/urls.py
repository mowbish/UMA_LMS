from django.urls import path
from .views import ShowCollagesAPIView, ShowFacultyAPIView, CreateStudentAPIView, CreateProfessorAPIView, \
    CreateLessonAPIView, CreateRoomAPIView, show_rooms, room_detail

urlpatterns = [
    path('collages/', ShowCollagesAPIView.as_view({'get': 'list'})),
    path('faculties/', ShowFacultyAPIView.as_view({'get': 'list'})),
    path('signup/student/', CreateStudentAPIView.as_view()),
    path('signup/professor/', CreateProfessorAPIView.as_view()),
    path('create/lesson/', CreateLessonAPIView.as_view()),
    path('create/room/', CreateRoomAPIView.as_view()),

    path('rooms/', show_rooms, name="rooms"),
    path('rooms/<slug:slug>', room_detail, name="room_detail"),
    # path('rooms/', go_to_room, name="room_detail"),
]
