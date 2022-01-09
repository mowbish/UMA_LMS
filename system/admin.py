from django.contrib import admin
from .models import (Collage, Faculty, Class, Person, Professor, Student, Lesson, Task)

admin.site.register(Collage)


class CollageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Faculty)


class FacultyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Class)


class ClassAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person)


class PersonAdmin(admin.ModelAdmin):
    pass


admin.site.register(Professor)


class ProfessorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Student)


class StudentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Lesson)


class LessonAdmin(admin.ModelAdmin):
    pass


admin.site.register(Task)


class TaskAdmin(admin.ModelAdmin):
    pass
