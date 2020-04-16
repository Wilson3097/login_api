from rest_framework import status
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer, LoginSerializer
# from rest_framework.authtoken.models import Token
from .csrf_chceck import *
# from rest_framework.authentication import BasicAuthentication
# from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.contrib.auth.models import User


@csrf_exempt
@api_view(['POST'])
def registration_view(request):

    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Succesfully registered a user"
            data['email'] = user.email
            data['username'] = user.username
            data['password'] = user.password
            return Response(data, status=status.HTTP_201_CREATED)

        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = LoginSerializer(data=data)
        # if not serializer.is_valid():
        #     raise ValidationError(serializer.errors)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
