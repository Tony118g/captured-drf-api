from django.db import IntegrityError
from rest_framework import serializers
from .models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    """
    Provides readability for attendance data in API.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    class Meta:
        model = Attendance
        fields = [
            'id',
            'created_at',
            'owner',
            'tour',
            'profile_id',
            'profile_image'
        ]

    def create(self, validate_data):
        """
        Displays an error message when a user tries
        to mark the same tour as attending more than once.
        """
        try:
            return super().create(validate_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
