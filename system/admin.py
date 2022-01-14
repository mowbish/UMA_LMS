from django.contrib import admin
from .models import (Collage, Faculty, Class, Person, Professor, Student, Lesson, Task, ScientificGroup)
from django.contrib.auth.admin import UserAdmin


@admin.register(Collage)
class CollageAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    # exclude = ("slug",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(ScientificGroup)
class ScientificGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'phone_number', 'is_staff',
        'is_professor', 'is_student', 'mailing_address', 'date_joined', 'last_login'
    )
    list_filter = ('is_student', 'is_professor')
    ordering = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'email')
    prepopulated_fields = {"slug": ('first_name', 'last_name', 'username')}


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # prepopulated_fields = {"slug": (,)}
    pass


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass
    # prepopulated_fields = {"slug": ("label","unit")}


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


UserAdmin.fieldsets[1][1]['fields'] = (
    'first_name',
    'last_name',
    'email',
    'phone_number',
)

# Admin can not change user account information
UserAdmin.readonly_fields = (
    'username',
    'first_name',
    'last_name',
    'email',
    'phone_number',
    'last_login',
    'date_joined'
)

UserAdmin.list_display += ('phone_number',)
