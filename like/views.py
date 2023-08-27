from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from post.models import Post
from .models import Like
from .serializer import LikeSerializer
from drf_yasg.utils import swagger_auto_schema


# Create your views here.

class LikeView(APIView):
    @swagger_auto_schema(
        request_body=LikeSerializer,
        responses={
            status.HTTP_201_CREATED: LikeSerializer(),
            status.HTTP_400_BAD_REQUEST: "You have already liked this post."
        }
    )
    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)

        if Like.objects.filter(post=post, user=request.user).exists():
            return Response({"error": "You have already liked this post."},
                            status=status.HTTP_400_BAD_REQUEST)

        like = Like(post=post, user=request.user)
        like.save()

        serializer = LikeSerializer(like)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UnlikeView(APIView):
    @swagger_auto_schema(
        responses={
            status.HTTP_204_NO_CONTENT: "You have unliked the post.",
            status.HTTP_400_BAD_REQUEST: "You have not liked this post."
        }
    )
    def delete(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)

        like = Like.objects.filter(post=post, user=request.user).first()
        if like:
            like.delete()
            return Response({"message": "You have unliked the post."},
                            status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "You have not liked this post."},
                            status=status.HTTP_400_BAD_REQUEST)
