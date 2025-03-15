from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import CustomUserSerializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class LoginAPIView(APIView):
    def post(self,request):
        serializer = CustomUserSerializers(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username,password=password)

            if user is not None:
                refresh = RefreshToken.for_user(user=user)

                return Response(
                    {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                    }
                    , status=status.HTTP_200_OK
                )
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
