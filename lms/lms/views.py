from urllib import request
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status

class Login(ObtainAuthToken):

    def post(self, request,*args,**kwargs):
        login_serializer = self.serializer_class(data = request.data, context = {'request':request})
        if login_serializer.is_valid():
            print(login_serializer.validated_data['user'])
        return Response({'mensaje': 'Este es el response'}, status = status.HTTP_200_OK)

        