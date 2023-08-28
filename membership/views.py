from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Membership
from .serializer import MembershipSerializer, UserSerializer, GroupSerializer


# Create your views here.
class MembershipListView(APIView):
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="List of memberships",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                        'user': UserSerializer(),
                        'groups': GroupSerializer(),
                        'joined_at': openapi.Schema(type=openapi.TYPE_STRING, format='date-time'),
                        'left_at': openapi.Schema(type=openapi.TYPE_STRING, format='date-time'),
                        'created_at': openapi.Schema(type=openapi.TYPE_STRING, format='date-time'),
                        'updated_at': openapi.Schema(type=openapi.TYPE_STRING, format='date-time'),
                    }),
                ),
            )
        },
    )
    def get(self, request):
        memberships = Membership.objects.all()
        serializer = MembershipSerializer(memberships, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MembershipView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'user': UserSerializer(),
                'groups': GroupSerializer(),
                'joined_at': openapi.Schema(type=openapi.TYPE_STRING, format='date-time'),
                'left_at': openapi.Schema(type=openapi.TYPE_STRING, format='date-time'),
            }
        ),
        responses={
            status.HTTP_201_CREATED: "Membership created successfully",
            status.HTTP_400_BAD_REQUEST: "Invalid input data"
        }
    )
    def post(self, request):
        serializer = MembershipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MembershipDetailView(APIView):
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Membership details",
                schema=MembershipSerializer()
            ),
            status.HTTP_404_NOT_FOUND: "Membership not found"
        }
    )
    def get(self, request, membership_id):
        try:
            membership = Membership.objects.get(pk=membership_id)
        except Membership.DoesNotExist:
            raise NotFound("Membership not found")

        serializer = MembershipSerializer(membership)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateMembersView(APIView):
    @swagger_auto_schema(
        request_body=MembershipSerializer,
        responses={
            status.HTTP_200_OK: "Membership updated successfully",
            status.HTTP_400_BAD_REQUEST: "Invalid input data",
            status.HTTP_404_NOT_FOUND: "Membership not found"
        }
    )
    def put(self, request, membership_id):
        try:
            membership = Membership.objects.get(pk=membership_id)
        except Membership.DoesNotExist:
            raise NotFound("Membership not found")

        serializer = MembershipSerializer(membership, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteMembershipView(APIView):
    @swagger_auto_schema(
        responses={
            status.HTTP_204_NO_CONTENT: "Membership deleted successfully",
            status.HTTP_404_NOT_FOUND: "Membership not found"
        }
    )
    def delete(self, request, membership_id):
        try:
            membership = Membership.objects.get(pk=membership_id)
        except Membership.DoesNotExist:
            raise NotFound("Membership not found")

        membership.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
