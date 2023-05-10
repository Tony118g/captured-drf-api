from rest_framework import serializers
from .models import Tour


class TourSerializer(serializers.ModelSerializer):
    """
    Provides readability for tour data in API.
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    guide = serializers.CharField(default='currently unknown')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')

    def validate_image(self, value):
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

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Tour
        fields = [
            'id',
            'owner',
            'title',
            'description',
            'country',
            'city',
            'time_period',
            'guide',
            'price',
            'booking_means',
            'image',
            'created_at',
            'updated_at',
            'is_owner',
            'profile_id',
        ]
