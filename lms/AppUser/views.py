from os import stat
from django import views
from rest_framework.response import Response
from rest_framework.views import APIView
from lms.serializer import PostCustomUser
from .models import customUser
from rest_framework import status
from django.http import Http404

class customerUser_APIView(APIView):

    def get(self, request, format=None, *args, **kwargs):
        post = customUser.objects.all()
        serializer = PostCustomUser(post, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostCustomUser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

class customerUser_APIView_Detail(APIView):

    def get_object(self, pk):
        try:
            return customUser.objects.get(pk=pk)
        except customUser.DoesNotExist:
            raise Http404
    def get (self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostCustomUser (post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        post= self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)