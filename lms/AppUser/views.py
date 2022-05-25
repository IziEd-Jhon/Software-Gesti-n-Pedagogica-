from os import stat
<<<<<<< Updated upstream
from django import views
from rest_framework.response import Response
from rest_framework.views import APIView
from lms.serializer import *
from .models import Teacher, customUser, Parent
from rest_framework import status
from django.http import Http404
=======
from AppUser.serializer import CustomEnrollmentCourseSerializer, CustomEnrollmentSubjectSerializer, CustomParentSerializer,CustomStudentSerializer,CustomTeacherSerializer,CustomAnnotationSerializer
from .models import Annotation, EnrollmentCourse, Teacher, customUser, Parent, EnrollmentSubject
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
    permission_classes=[permissions.IsAuthenticated]
=======
    permission_classes=[permissions.IsAuthenticated]

class ParentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Parent.objects.all()
    serializer_class=CustomParentSerializer
    permission_classes=[permissions.IsAuthenticated]

#Vista generia de Anotaciones
class AnnotationList(generics.ListCreateAPIView):
    queryset= Annotation.objects.all()
    serializer_class=CustomAnnotationSerializer
    permission_classes = [permissions.IsAuthenticated]

class AnnotationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Annotation.objects.all()
    serializer_class=CustomAnnotationSerializer
    permission_classes=[permissions.IsAuthenticated]

#Vista Generica de Cursando Materias 
class EnrollmentSubjectList(generics.ListCreateAPIView):
    queryset = EnrollmentSubject.objects.all() 
    serializer_class = CustomEnrollmentSubjectSerializer
    permission_classes = [permissions.IsAuthenticated]

class EnrollmentSubjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EnrollmentSubject.objects.all()
    serializer_class = CustomEnrollmentSubjectSerializer
    permission_classes = [permissions.IsAuthenticated]

#Vista generica Cursando Materias
class EnrollmentCourseList(generics.ListCreateAPIView):
    queryset = EnrollmentCourse.objects.all()
    serializer_class = CustomEnrollmentCourseSerializer
    permission_classes = [permissions.IsAuthenticated]

class EnrollmentCourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EnrollmentCourse.objects.all()
    serializer_class = CustomEnrollmentCourseSerializer
    permission_classes = [permissions.IsAuthenticated]


>>>>>>> Stashed changes
