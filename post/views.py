from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .models import Post
from .serializer import CreatPost, UpdatePostSerializer


# Create your views here.

class CreatePostView(APIView):
    @swagger_auto_schema(
        operation_description='Create a new post',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'content': openapi.Schema(type=openapi.TYPE_STRING, description='new post'),
                'image': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY),
                'video': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY),
            }
        ),
        responses={
            201: 'Created successfully',
            400: 'Bad request',
            401: 'Unauthorized',
            403: 'Forbidden',
            500: 'Internal Server Error',
        }
    )
    def post(self, request):
        serializer = CreatPost(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdatePostView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = UpdatePostSerializer

    @swagger_auto_schema(
        operation_description='Update post',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'content': openapi.Schema(type=openapi.TYPE_STRING, description='new post'),
                'image': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY),
                'video': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY),

            }

        ),
        responses={
            200: 'Post Update Success',
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden",
            404: "Not Found",
            500: "Internal Server Error",
        }

    )
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeletePostView(APIView):
    @swagger_auto_schema(
        operation_description='Delete a post',
        responses={
            204: 'Post Deleted',
            404: 'Post Not Found',

        }
    )
    def delete(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            if post.user == request.user:
                post.delete()
                return Response({'Message': "Post Deleted"}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'Error': "Yod are not allowed to delete"}, status=status.HTTP_403_FORBIDDEN)
        except Post.DoesNotExist:
            return Response({'Error': 'Post Not Found'}, status=status.HTTP_404_NOT_FOUND)
