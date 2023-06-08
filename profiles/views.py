from django.db.models import Count
from rest_framework import generics, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from captured_drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.response import Response


class ProfileList(generics.ListAPIView):
    """
    Lists all profiles.
    """
    queryset = Profile.objects.annotate(
        photos_count=Count('owner__photo', distinct=True),
        followers_count=Count(
            'owner__followed',
            distinct=True
            ),
        following_count=Count(
            'owner__following',
            distinct=True
        )
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile',
    ]

    ordering_fields = [
        'photos_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving and updating profiles by id if owned.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        photos_count=Count('owner__photo', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer

    def perform_destroy(self, instance):
        """
        Deletes the profile owner's user account when the profile is deleted.
        """
        user = instance.owner
        user.delete()
