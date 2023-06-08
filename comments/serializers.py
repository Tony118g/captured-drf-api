from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializes comment data.
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Returns true if the user is the object owner.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        """
        Returns the time elapsed since the comment was created.
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """
        Returns the time elapsed since the comment was updated.
        """
        return naturaltime(obj.updated_at)

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
    Serializer for the Comment model used in the Detail view.
    """
    photo = serializers.ReadOnlyField(source='photo.id')
