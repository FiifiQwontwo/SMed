from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializer import AccountSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.

# class RegisterAPIView(APIView):
#     @swagger_auto_schema(
#         request_body=AccountSerializer,
#         responses={
#             status.HTTP_201_CREATED: "User registered successfully",
#             status.HTTP_400_BAD_REQUEST: "Invalid input data"
#         }
#     )
#     def post(self, request):
#         serializer = AccountSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#
#             refresh = RefreshToken.for_user(user)
#             access_token = str(refresh.access_token)
#
#             return Response({
#                 "message": "User registered successfully",
#                 "access_token": access_token,
#             }, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterAPIView(APIView):
    @swagger_auto_schema(
        request_body=AccountSerializer,
        responses={
            status.HTTP_201_CREATED: "User registered successfully",
            status.HTTP_400_BAD_REQUEST: "Invalid input data"
        }
    )
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD)
            }
        ),
        responses={
            status.HTTP_200_OK: "Login successful",
            status.HTTP_401_UNAUTHORIZED: "Invalid credentials"
        }
    )
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# class LoginAPIView(APIView):
#     @swagger_auto_schema(
#         request_body=openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             properties={
#                 'username': openapi.Schema(type=openapi.TYPE_STRING),
#                 'password': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD)
#             }
#         ),
#         responses={
#             status.HTTP_200_OK: "Login successful",
#             status.HTTP_401_UNAUTHORIZED: "Invalid credentials"
#         }
#     )
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)
#
#         if user:
#             refresh = RefreshToken.for_user(user)
#             access_token = str(refresh.access_token)
#
#             return Response({
#                 "message": "Login successful",
#                 "access_token": access_token,
#             }, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserManagementAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: AccountSerializer(),
            status.HTTP_401_UNAUTHORIZED: "Authentication credentials were not provided"
        }
    )
    def get(self, request):
        serializer = AccountSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=AccountSerializer,
        responses={
            status.HTTP_200_OK: "User information updated successfully",
            status.HTTP_400_BAD_REQUEST: "Invalid input data",
            status.HTTP_401_UNAUTHORIZED: "Authentication credentials were not provided"
        }
    )
    def put(self, request):
        serializer = AccountSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
