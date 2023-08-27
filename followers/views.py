from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from .models import UserFollow
from .serializer import UserFollowSerializer


# Create your views here.


class FollowUserView(APIView):
    @swagger_auto_schema(
        request_body=UserFollowSerializer,
        responses={
            status.HTTP_201_CREATED: openapi.Response(
                description="User followed successfully"
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Bad request"
            ),
        },
    )
    def post(self, request):
        serializer = UserFollowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UnfollowUserView(APIView):

    @swagger_auto_schema(
        responses={
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description="User unfollowed successfully"
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="User not found or not being followed"
            ),
        },
    )
    def delete(self, request, user_id):
        try:
            follow = UserFollow.objects.get(follower=request.user, following_id=user_id)
        except UserFollow.DoesNotExist:
            raise NotFound("You are not following this user.")

        follow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
