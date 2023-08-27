from rest_framework import serializers
from .models import Repost


class RepostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repost
        fields = ('id', 'post', 'user', 'created_at')
