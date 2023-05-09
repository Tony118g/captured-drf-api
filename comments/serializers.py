from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Provides readability for comment data in API.
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Comment
        fields = [
            'id',
            'owner',
            'is_owner',
            'photo',
            'content',
            'created_at',
            'updated_at',
            'profile_id',
            'profile_image',
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model used in the Detail view
    """
    photo = serializers.ReadOnlyField(source='photo.id')
