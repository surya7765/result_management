from rest_framework import serializers
from stapi.models import Student, Subject, SubMarks
from django.contrib.auth import get_user_model


# serialize relations between Student Subject and Submarks

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = ['password', 'last_login', 'is_superuser', 'is_staff',
                   'is_active', 'date_joined', 'groups', 'user_permissions']


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Student
        exclude = ['registration_number',
                   'class_name', 'father_name', 'mother_name', 'address', 'phone','marks']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['user']

class SubMarksSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    class Meta:
        model = SubMarks
        fields = ('student','subject','obtained_marks','total_marks')
        depth = 2

class StudentDataSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    subjects = SubjectSerializer(many=True, read_only=True)
    submarks = SubMarksSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['user', 'registration_number',
                  'class_name', 'father_name', 'mother_name', 'address', 'phone', 'subjects', 'submarks']
        depth = 1

