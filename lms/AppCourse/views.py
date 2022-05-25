from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .models import Course
from AppCourse.serializer import *

# Create your views here.

#Vista generica de los Cursos
class CourseList(generics.ListCreateAPIView):
    queryset=Course.objects.all()
    serializer_class=CustomCourseSerializer
    permission_classes=[permissions.IsAuthenticated]

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Course.objects.all()
    serializer_class=CustomCourseSerializer
    permission_classes=[permissions.IsAuthenticated]