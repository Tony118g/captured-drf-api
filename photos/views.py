from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from captured_drf_api.permissions import IsOwnerOrReadOnly
from .models import Photo
from .serializers import PhotoSerializer


class PhotoList(generics.ListCreateAPIView):
    """
    Lists photos and handles creation of a photo if logged in.
    """

    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Photo.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
    ]

    search_fields = [
        'owner__username',
        'title',
    ]

    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating and deleting photos by id if owned.
    """
    serializer_class = PhotoSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Photo.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
