from rest_framework import serializers
from .models import Post


class CreatPost(serializers.ModelSerializer):
    image = serializers.FileField(required=False)
    video = serializers.FileField(required=False)

    class Meta:
        model = Post
        fields = '__all__'

    def save(self, *args, **kwargs):
        content = self.validated_data.get('content')
        image = self.validated_data.get('image')
        video = self.validated_data.get('video')
        user = self.context['request'].user

        new_post = Post(
            content=content,
            image=image,
            video=video,
            user=user
        )
        new_post.save()
        return new_post


class UpdatePostSerializer(serializers.ModelSerializer):
    image = serializers.FileField(required=False)
    video = serializers.FileField(required=False)

    class Meta:
        model = Post
        fields = '__all__'

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance


class PostDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
