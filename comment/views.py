from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from .serializer import CommentSerializer, CommentForUserSerializer, CommentForPostSerializer
from drf_yasg.utils import swagger_auto_schema
from django.core.exceptions import ObjectDoesNotExist


class CreateCommentView(APIView):
    @swagger_auto_schema(
        request_body=CommentSerializer,
        responses={
            status.HTTP_201_CREATED: CommentSerializer(),
            status.HTTP_400_BAD_REQUEST: "Bad Request"
        }
    )
    def post(self, request):
        try:
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)  # Assuming you're using authentication
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CommentsForUserView(APIView):
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: CommentForUserSerializer(many=True),
            status.HTTP_404_NOT_FOUND: "User not found"
        }
    )
    def get(self, request, user_id):
        try:
            comments = Comment.get_comments_for_user(user_id)
            serializer = CommentForUserSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CommentsForPostView(APIView):
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: CommentForPostSerializer(many=True),
            status.HTTP_404_NOT_FOUND: "Post not found",
            status.HTTP_500_INTERNAL_SERVER_ERROR: "Internal server error"
        }
    )
    def get(self, request, post_id):
        try:
            comments = Comment.get_comments_for_post(post_id)
            serializer = CommentForPostSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

