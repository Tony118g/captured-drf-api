from django.db.models import Count
from rest_framework import generics, filters
from captured_drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    Lists all profiles.
    """

    queryset = Profile.objects.annotate(
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
        filters.OrderingFilter
    ]
    ordering_fields = [
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Handles retrieving and updating profiles by id if owned
    """

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
