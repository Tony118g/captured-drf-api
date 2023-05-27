from rest_framework import serializers
from .models import Tour
from attendances.models import Attendance
from datetime import date, datetime, timedelta

TOMORROW = date.today() + timedelta(days=1)


class TourSerializer(serializers.ModelSerializer):
    """
    Provides readability for tour data in API.
    """

    start_date = serializers.DateField(
        error_messages={
            'invalid': 'Please input a valid date with format: dd/mm/yyyy.'
            }
        )
    end_date = serializers.DateField(
        error_messages={
            'invalid': 'Please input a valid date with format: dd/mm/yyyy.'
            }
        )
    owner = serializers.ReadOnlyField(source='owner.username')
    guide = serializers.CharField(default='currently unknown')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    attendance_id = serializers.SerializerMethodField()
    attendance_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value:
            if value.size > 2 * 1024 * 1024:
                raise serializers.ValidationError('Image size larger than 2MB!')
            if value.image.height > 4096:
                raise serializers.ValidationError(
                    'Image height larger than 4096px!'
                )
            if value.image.width > 4096:
                raise serializers.ValidationError(
                    'Image width larger than 4096px!'
                )
        return value

    def validate_start_date(self, value):
        if value < TOMORROW:
            raise serializers.ValidationError(
                "Start date cannot be a present or past date."
                )
        return value

    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError(
                {"end_date": "End date must be after start date."}
                )
        return data

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_attendance_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            attendance = Attendance.objects.filter(
                owner=user, tour=obj
            ).first()
            return attendance.id if attendance else None
        return None

    class Meta:
        model = Tour
        fields = [
            'id',
            'owner',
            'title',
            'description',
            'country',
            'city',
            'start_date',
            'end_date',
            'guide',
            'price',
            'booking_means',
            'image',
            'created_at',
            'updated_at',
            'is_owner',
            'profile_id',
            'attendance_id',
            'attendance_count',
        ]
