from os import stat
from tokenize import String
from rest_framework.response import Response
from AppUser.serializer import CustomParentSerializer, CustomStudentSerializer, CustomTeacherSerializer, FileUploadSerializer
from AppUser.models import Teacher, customUser, Parent
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from rest_framework.exceptions import UnsupportedMediaType
import io, csv, pandas as pd

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