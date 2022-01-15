import random
import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, User
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator


class Collage(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=200)
    collage = models.ForeignKey(Collage, on_delete=models.CASCADE)
    dean = models.CharField(max_length=45, unique=True)
    detail = models.TextField()
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('system:faculties', args=self.slug)


class ScientificGroup(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, db_index=True, unique=True, blank=True, null=True, )
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ScientificGroups'
        verbose_name = 'ScientificGroup'
        verbose_name_plural = 'ScientificGroups'

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        # Raise on circular reference
        parent = self.parent
        while parent is not None:
            if parent == self:
                raise RuntimeError("Circular references not allowed")
            parent = parent.parent

        super(ScientificGroup, self).save(*args, **kwargs)

    @property
    def children(self):
        return self.ScientificGroup_set.all().order_by("title")


class Professor(User):
    slug = models.SlugField(max_length=50, unique=True, null=True, blank=True)
    phone_number_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$", message='Must enter a valid phone number')
    phone_number = models.CharField(validators=[phone_number_regex], max_length=16, blank=True)
    levels = (
        (1, "lecturer"),
        (2, "assistant_professors"),
        (3, "associate_professors"),
        (4, "full_professors"),
    )

    rank_of_professor = models.IntegerField(choices=levels)
    teaching_area = models.ForeignKey(ScientificGroup, on_delete=models.CASCADE)
    mailing_address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.username


class Student(User):
    slug = models.SlugField(max_length=50, unique=True, null=True, blank=True)
    phone_number_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$", message='Must enter a valid phone number')
    phone_number = models.CharField(validators=[phone_number_regex], max_length=16, blank=True)
    CHOICES = (
        (1, "Bachelor"),
        (2, "Master"),
        (3, "PhD"),
    )
    grade = models.IntegerField(choices=CHOICES)
    student_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    entered_time = models.DateField(auto_now=True, editable=False)
    term = models.PositiveSmallIntegerField(default=1)
    mailing_address = models.CharField(max_length=200, blank=True)
    image = models.FileField(upload_to="media/student_profiles/", blank=True, null=True)

    def __str__(self):
        return self.username


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
    unit = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    slug = models.SlugField(max_length=50, unique=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name='student_lesson')
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    CHOICES = (
        (1, "exclusive"),
        (2, "general")
    )
    lesson_type = models.PositiveSmallIntegerField(choices=CHOICES)
    class_of_lesson = models.ManyToManyField(Class)
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label


class Content(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=220)
    description = models.TextField()
    image = models.FileField(upload_to="media/Contents/", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)


class Task(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=220)
    description = models.TextField()
    image = models.FileField(upload_to="media/Tasks/", blank=True, null=True)
    score = models.SmallIntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)
    expires = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
