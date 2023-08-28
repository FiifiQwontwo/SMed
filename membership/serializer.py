from django.contrib.auth.models import User
from rest_framework import serializers
from groups.models import Group
from .models import Membership


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class MembershipSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    groups = GroupSerializer()

    class Meta:
        model = Membership
        fields = ['user', 'groups', 'joined_at', 'left_at', 'created_at', 'updated_at']
