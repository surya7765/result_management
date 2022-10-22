from django.shortcuts import render
from rest_framework import viewsets
from stapi.models import Student, Subject, SubMarks
from stapi.serializers import StudentSerializer, SubjectSerializer, SubMarksSerializer
from rest_framework.response import Response

# Create your views here.

def Home(request):
  return render(request, 'stapi/home.html')


# make view which returns data of current logged in user
class StudentViewSet(viewsets.ModelViewSet):
  serializer_class = StudentSerializer
  http_method_names = ['get']

  def get_queryset(self):
    # return current user details
    # print(self.request.user.is_superuser)
    if self.request.user.is_superuser:
      return Student.objects.all()
    else:
      return Student.objects.all().filter(user=self.request.user)
