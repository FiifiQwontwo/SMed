from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .models import Repost
from .serializer import RepostSerializer


# Create your views here.

class RepostView(APIView):
    @swagger_auto_schema(
        request_body=RepostSerializer,
        responses={
            status.HTTP_201_CREATED: "Repost created successfully.",
            status.HTTP_400_BAD_REQUEST: "Validation error.",
        }
    )
    def post(self, request):
        serializer = RepostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
