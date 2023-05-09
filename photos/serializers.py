from rest_framework import serializers
from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    """
    Provides readability for photo data in API.
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    camera_used = serializers.CharField(default='unstated')
    lense_used = serializers.CharField(default='unstated')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

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
        model = Photo
        fields = [
            'id',
            'owner',
            'title',
            'camera_used',
            'lense_used',
            'description',
            'image',
            'created_at',
            'updated_at',
            'is_owner',
            'profile_id',
            'profile_image',
        ]