from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


class Collage(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=200)
    collage = models.ForeignKey(Collage, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('system:faculties', args=self.slug)


class Person(AbstractUser):
    phone_number_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$", message=_('Must enter a valid phone number'))
    phone_number = models.CharField(validators=[phone_number_regex], max_length=16, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    is_student = models.BooleanField(default=False)
    is_professor = models.BooleanField(default=False)


class Professor(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    
    teaching_area = models.ForeignKey()
    # faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Student(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, unique=True)
    Bachelor = "Bachelor"
    Master = "Master"
    PhD = "PhD"
    CHOICES = (
        (Bachelor, "Bachelor"),
        (Master, "Master"),
        (PhD, "PhD"),
    )
    grade = models.CharField(max_length=10, choices=CHOICES)

    image = models.FileField(upload_to="media/student_profiles/", blank=True, null=True)

    def __str__(self):
        return self.user.username


class Class(models.Model):
    name = models.CharField(max_length=200)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    CHOICES = (
        (1, 'activate'),
        (2, 'deactivate'),
    )
    status = models.PositiveSmallIntegerField(choices=CHOICES)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    label = models.CharField(max_length=200)
    term = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(14)])
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name='student_lesson')
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    exclusive = 1
    general = 2
    CHOICES = (
        (exclusive, "exclusive"),
        (general, "general")
    )
    lesson_type = models.PositiveSmallIntegerField(choices=CHOICES)
    class_of_lesson = models.ManyToManyField(Class)
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label


class Task(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=220)
    description = models.TextField()
    image = models.FileField(upload_to="media/Tasks/", blank=True, null=True)
    score = models.SmallIntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)
    expires = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
