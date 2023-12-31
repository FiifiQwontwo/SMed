from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from membership.models import Membership
from .models import Group
from .serializer import CreateGroup, GroupSerializer
from django.shortcuts import get_object_or_404


class CreateGroupView(APIView):

    @swagger_auto_schema(
        operation_description='Create a group',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='new Group'),
                'description': openapi.Schema(type=openapi.TYPE_STRING, description='Description of group'),
            }
        ),
        responses={
            201: 'Create Group',
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            500: 'Internal Server Error',
        }
    )
    def post(self, request):
        serializer = CreateGroup(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ManageGroupsView(APIView):
    def get(self, request, format=None):
        user = request.user
        groups = Group.objects.filter(membership__user=user)
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            group = serializer.save()
            Membership.objects.create(user=request.user, group=group)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LeaveGroupView(APIView):
    def post(self, request, membership_id, ):
        membership = get_object_or_404(Membership, pk=membership_id)

        if membership.user != request.user:
            return Response({"message": "You are not authorized to leave this group."},
                            status=status.HTTP_403_FORBIDDEN)

        membership.delete()

        return Response({"message": "You have successfully left the group."},
                        status=status.HTTP_200_OK)
