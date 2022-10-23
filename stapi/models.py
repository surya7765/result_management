from django.db import models
# import User
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

CLASS_CHOICE = [
  ('NURSERY','NURSERY'),
  ('KG','KG'),
  ('STD_ONE','STD_ONE'),
  ('STD_TWO','STD_TWO'),
  ('STD_THREE','STD_THREE'),
  ('STD_FOUR','STD_FOUR'),
]

class Student(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
  registration_number = models.CharField(max_length=30,unique=True)
  class_name = models.CharField(choices=CLASS_CHOICE,max_length=10)
  father_name = models.CharField(max_length=30)
  mother_name = models.CharField(max_length=30)
  address = models.TextField()
  phone = models.IntegerField()
  marks = models.ManyToManyField('Subject', through='SubMarks')

  def __str__(self):
    return self.user.username



class Subject(models.Model):
  subject_name = models.CharField(max_length=30)

  def __str__(self):
    return self.subject_name



class SubMarks(models.Model):
  student = models.ForeignKey(Student,related_name= 'submarks',on_delete=models.CASCADE)
  subject = models.ForeignKey(Subject, related_name='subjects' ,on_delete=models.CASCADE,default=1)
  obtained_marks = models.IntegerField(blank=True, null=True, validators=[
      MaxValueValidator(100),
      MinValueValidator(1)
  ])
  total_marks = models.IntegerField(default=100, validators=[
      MaxValueValidator(100),
      MinValueValidator(1)
  ])
  
  def __str__(self):
    return self.subject.subject_name
