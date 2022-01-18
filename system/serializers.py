from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import (Collage, Faculty, ScientificGroup,
                     Professor, Student, Class,
                     Lesson, Content, Task, )


class CollageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collage
        fields = ("name",)


class FacultySerializer(serializers.ModelSerializer):
    collage = serializers.StringRelatedField()

    class Meta:
        model = Faculty
        fields = ('name', 'collage', 'dean', 'detail', 'slug')


class ScientificGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScientificGroup
        fields = "__all__"


class CreateProfessorSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Student.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Professor
        fields = (
            'username', 'password', 'password2', 'email', 'first_name', 'last_name',
            'rank_of_professor', 'teaching_area'
        )
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        professor = Professor.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            rank_of_professor=validated_data['rank_of_professor'],
            teaching_area=validated_data['teaching_area'],
            is_staff=True
        )

        professor.set_password(validated_data['password'])
        professor.save()

        return professor


class CreateStudentSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Student.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Student
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'grade',
                  )
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        student = Student.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            grade=validated_data['grade']
        )

        student.set_password(validated_data['password'])
        student.save()

        return student


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
