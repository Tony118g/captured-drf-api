from rest_framework import serializers
from .models import Photo
from likes.models import Like


class PhotoSerializer(serializers.ModelSerializer):
    """
    Serializes photo data.
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    camera_used = serializers.CharField(default='unstated')
    lense_used = serializers.CharField(default='unstated')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        """
        Validates whether the image is the correct size.
        """
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
        """
        Returns true if the user is the object owner.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        """
        Returns the id of the relevant like for the user and photo.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, photo=obj
            ).first()
            return like.id if like else None
        return None

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
            'like_id',
            'likes_count',
            'comments_count',
        ]
