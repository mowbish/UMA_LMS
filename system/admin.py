from django.contrib import admin
from .models import (Collage, Faculty, Class, Professor, Student, Lesson, Task, ScientificGroup)
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


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'phone_number',
        'mailing_address', 'date_joined', 'last_login'
    )
    list_filter = ('rank_of_professor',)
    ordering = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    prepopulated_fields = {"slug": ('first_name', 'last_name', 'username', 'phone_number')}


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'phone_number',
        'student_number', 'term', 'mailing_address', 'date_joined', 'last_login'
    )
    list_filter = ('grade',)
    ordering = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    prepopulated_fields = {"slug": ('first_name', 'last_name', 'username', 'phone_number')}


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass
    # prepopulated_fields = {"slug": ("label","unit")}


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass

# UserAdmin.fieldsets[1][1]['fields'] = (
#     'first_name',
#     'last_name',
#     'email',
#     'phone_number',
# )
#
# # Admin can not change user account information
# UserAdmin.readonly_fields = (
#     'username',
#     'first_name',
#     'last_name',
#     'email',
#     'phone_number',
#     'last_login',
#     'date_joined'
# )
#
# UserAdmin.list_display += ('phone_number',)
