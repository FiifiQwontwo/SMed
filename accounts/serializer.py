from rest_framework import serializers

from .models import Account, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('profile_pic',)


class AccountSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(source='userprofile', read_only=True)

    class Meta:
        model = Account
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'phone', 'date_joined', 'last_login',
                  'is_admin', 'is_active', 'is_superuser', 'is_staff', 'user_profile')

    def create(self, validated_data):
        user_profile_data = validated_data.pop('userprofile', None)
        account = Account.objects.create(**validated_data)
        if user_profile_data:
            UserProfile.objects.create(user=account, **user_profile_data)
        return account

    def update(self, instance, validated_data):
        user_profile_data = validated_data.pop('userprofile', None)
        instance = super().update(instance, validated_data)
        if user_profile_data:
            user_profile, created = UserProfile.objects.get_or_create(user=instance)
            for attr, value in user_profile_data.items():
                setattr(user_profile, attr, value)
            user_profile.save()
        return instance
