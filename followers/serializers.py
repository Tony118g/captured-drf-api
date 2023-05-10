from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    """
    Provides readability for follower data in API.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Follower
        fields = [
            'id',
            'owner',
            'followed',
            'created_at',
            'followed_name',
        ]

    def create(self, validated_data):
        """
        Displays an error message when a user tries
        to follow another user more than once.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                {'detail': 'possible duplicate'}
            )
