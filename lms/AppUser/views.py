from os import stat
from django import views
from rest_framework.response import Response
from rest_framework.views import APIView
from AppUser.serializer import CustomParentSerializer,CustomStudentSerializer,CustomTeacherSerializer
from .models import Teacher, customUser, Parent
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from rest_framework import permissions

#Vistas Genericas de Alumno
class StudentList(generics.ListCreateAPIView):
        queryset=customUser.objects.all()
        serializer_class=CustomStudentSerializer
        permission_classes=[permissions.IsAuthenticated]

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=customUser.objects.all()
    serializer_class=CustomStudentSerializer
    permission_classes=[permissions.IsAuthenticated]

#Vistas genericas de profes
class TeacherList(generics.ListCreateAPIView):
    queryset=Teacher.objects.all()
    serializer_class=CustomTeacherSerializer
    permission_classes=[permissions.IsAuthenticated]

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Teacher.objects.all()
    serializer_class=CustomTeacherSerializer
    permission_classes=[permissions.IsAuthenticated]

#Vista generica de Apoderados
class ParentList(generics.ListCreateAPIView):
    queryset=Parent.objects.all()
    serializer_class=CustomParentSerializer
    permission_classes=[permissions.IsAuthenticated]

class ParentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Parent.objects.all()
    serializer_class=CustomParentSerializer
    permission_classes=[permissions.IsAuthenticated]

