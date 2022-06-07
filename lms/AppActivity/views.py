from django.shortcuts import render
from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .models import *
from AppActivity.serializer import CustomResouresSerializer, CustomFolderSerializer, CustomArchiveSerializer, CustomActivitySerializer,CustomAssigmentSerializer , CustomQuizSerializer

# Create your views here.

class ResourceList(generics.ListCreateAPIView):
    queryset=Resource.objects.all()
    serializer_class=CustomResouresSerializer
    permission_classes=[permissions.IsAuthenticated]

class ResourceDetail(generics.RetrieveDestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class=CustomResouresSerializer
    permission_classes=[permissions.IsAuthenticated]

class FolderList(generics.ListCreateAPIView):
    queryset=Folder.objects.all()
    serializer_class=CustomFolderSerializer
    permission_classes=[permissions.IsAuthenticated]

class FolderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Folder.objects.all()
    serializer_class=CustomFolderSerializer
    permission_classes=[permissions.IsAuthenticated]

class ArchiveList(generics.ListCreateAPIView):
    queryset=Archive.objects.all()
    serializer_class=CustomArchiveSerializer
    permission_classes=[permissions.IsAuthenticated]

class ArchiveDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Archive.objects.all()
    serializer_class=CustomArchiveSerializer
    permission_classes=[permissions.IsAuthenticated]

class ActivityList(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class=CustomActivitySerializer
    permission_classes=[permissions.IsAuthenticated]

class ActivityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Activity.objects.all()
    serializer_class=CustomActivitySerializer
    permission_classes=[permissions.IsAuthenticated]

class AssigmentList(generics.ListCreateAPIView):
    queryset = Assigment.objects.all()
    serializer_class = CustomAssigmentSerializer
    permission_classes=[permissions.IsAuthenticated]

class AssigmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assigment.objects.all()
    serializer_class = CustomAssigmentSerializer
    permission_classes=[permissions.IsAuthenticated]

class QuizList(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = CustomQuizSerializer
    permission_classes=[permissions.IsAuthenticated]

class QuizDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = CustomQuizSerializer
    permission_classes=[permissions.IsAuthenticated]


    