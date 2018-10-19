from rest_framework import serializers

from users import models


class UserModelSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the UserModel objects."""

    class Meta:
        model = models.UserModel
        fields = ('name', 'url', 'email', 'password', 'created_at', 'updated_at')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'write_only': True},  # keeping the email write-only for privacy reasons
        }

    def create(self, validated_data):
        """Create and return a new user."""

        user = models.UserModel(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
