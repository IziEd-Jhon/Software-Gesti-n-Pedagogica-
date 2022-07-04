from __future__ import annotations
from os import stat
from tokenize import String

from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework.exceptions import UnsupportedMediaType
from rest_framework import generics, status, permissions, viewsets, request, filters

from AppUser.models import Teacher, customUser, Parent, EnrollmentCourse, Annotation, EnrollmentSubject

from AppUser.serializer import CustomParentSerializer,CustomStudentSerializer,CustomTeacherSerializer,CustomAnnotationSerializer, CustomEnrollmentSubject, CustomEnrollmentCourse, CustomUserSerializer, FileUploadSerializer

import io, csv, pandas as pd

#Vistas Genericas de Alumno
#class StudentList(generics.ListCreateAPIView):
#        queryset=customUser.objects.all()
#        serializer_class=CustomStudentSerializer
#        permission_classes=[permissions.IsAuthenticated]


#class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
#    queryset=customUser.objects.all()
#    serializer_class=CustomStudentSerializer
#    permission_classes=[permissions.IsAuthenticated]
#Crear usuario
@api_view(['POST'])
def UserCreate(request):
    serializer = CustomUserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response({'message':'Usuario creado correctamente'}, status = status.HTTP_201_CREATED)

#Vistas Manuales de Alumno

@api_view(['GET'])
def StudentList(request):
    queryset=customUser.objects.all()
    serializer = CustomStudentSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def StudentDetail(request, pk):
    queryset = customUser.objects.get(id=pk)
    serializer= CustomStudentSerializer(queryset, many=False)
    return Response(serializer.data)



@api_view(['POST'])
def StudentUpdate(request, pk):
    queryset = customUser.objects.get(id=pk)
    serializer= CustomStudentSerializer(instance=queryset, data = request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def StudentDelete(request, pk):
    queryset = customUser.objects.get(id=pk)
    queryset.delete()

    return Response ('Deleted')
######################################################################


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

#Vista generica Anotaciones
class AnnotationList(generics.ListCreateAPIView):
    queryset = Annotation.objects.all()
    serializer_class=CustomAnnotationSerializer
    permission_classes=[permissions.IsAuthenticated]

class AnnotationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Annotation.objects.all()
    serializer_class = CustomAnnotationSerializer
    permission_classes=[permissions.IsAuthenticated]

#Vista generica Cursando Materias
class EnrollmentSubjectList(generics.ListCreateAPIView):
    queryset = EnrollmentSubject.objects.all()
    serializer_class = CustomEnrollmentSubject
    permission_classes=[permissions.IsAuthenticated]

class EnrollmentSubjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EnrollmentSubject.objects.all()
    serializer_class = CustomEnrollmentSubject
    permission_classes=[permissions.IsAuthenticated]

#Vista Generica Cursando Cursos
class EnrollmentCourseList(generics.ListCreateAPIView):
    queryset = EnrollmentCourse.objects.all()
    serializer_class = CustomEnrollmentCourse
    permission_classes=[permissions.IsAuthenticated]

class EnrollmentCourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EnrollmentCourse.objects.all()
    serializer_class = CustomEnrollmentCourse
    permission_classes=[permissions.IsAuthenticated]

    
from AppUser.models import UploadUsersFromFile
class UploadUsersFromFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        file = serializer.validated_data['file']

        if not str(file).endswith('.csv'):
            raise UnsupportedMediaType(request.content_type, 
                detail={"base type" : f".{str(file).split('.')[-1]}",
                    "expected" : ".csv"}
            )

        reader = pd.read_csv(file, dtype=str)
        results = UploadUsersFromFile(reader, update_existing_users=True, create_users=True)

        return Response({"status": "success",
                        "file" : str(file),
                        "results" : results},
                        status.HTTP_201_CREATED)
