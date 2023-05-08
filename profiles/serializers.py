from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Provides readability for profile data in API.
    """

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile
        fields = [
            'id',
            'owner',
            'name',
            'description',
            'image',
            'created_at',
            'updated_at'
        ]
