from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'user', 'created_at')


class CommentForPostSerializer(serializers.ModelSerializer):
    post = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'content', 'post', 'user', 'created_at')

    def get_post(self, obj):
        return {
            'id': obj.post.id,
            'content': obj.post.content,
            'created_at': obj.post.created_at
        }


class CommentForUserSerializer(serializers.ModelSerializer):
    post = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'content', 'user', 'post', 'created_at')

    def get_post(self, obj):
        return {
            'id': obj.post.id,
            'content': obj.post.content,
            'created_at': obj.post.created_at
        }
