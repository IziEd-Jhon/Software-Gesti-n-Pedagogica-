from ast import Sub
from django.shortcuts import render
<<<<<<< Updated upstream

# Create your views here.
=======
from rest_framework import generics
from rest_framework import permissions
from .models import Course, Section, Subject
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

#Vista generica Materias
class SubjectList(generics.ListCreateAPIView):
    queryset=Subject.objects.all()
    serializer_class=CustomSubjectSerializer
    permission_classes=[permissions.IsAuthenticated]

class SubjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Subject.objects.all()
    serializer_class=CustomSubjectSerializer
    permission_classes=[permissions.IsAuthenticated]

#Vista Generica Secciones
class SectionList(generics.ListCreateAPIView):
    queryset=Section.objects.all()
    serializer_class = CustomSectionSerializer
    permission_classes = [permissions.IsAuthenticated]

class SectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Section.objects.all()
    serializer_class=CustomSectionSerializer
    permission_classes=[permissions.IsAuthenticated]
>>>>>>> Stashed changes
