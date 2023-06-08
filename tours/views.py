from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from captured_drf_api.permissions import IsAdminOrReadOnly
from .models import Tour
from .serializers import TourSerializer


class TourList(generics.ListCreateAPIView):
    """
    Lists tours and handles creation of a tour
    if logged in as an admin.
    """
    serializer_class = TourSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = Tour.objects.annotate(
        attendance_count=Count('attendances', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'attendances__owner__profile',
    ]

    search_fields = [
        'title',
        'country',
        'city',
    ]

    ordering_fields = [
        'attendance_count',
        'attendance__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TourDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles editing and deleting of tours by id
    if the user is the owner.
    """
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = TourSerializer
    queryset = Tour.objects.annotate(
        attendance_count=Count('attendances', distinct=True)
    ).order_by('-created_at')
