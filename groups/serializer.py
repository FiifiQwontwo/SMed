from rest_framework import serializers
from .models import Group


class CreateGroup(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model = Group
        fields = '__all__'

    def save(self, *args, **kwargs):
        name = self.validated_data.get('content')
        description = self.validated_data.get('image')

        new_group = Group(
            name=name,
            description=description,

        )
        new_group.save()
        return new_group
