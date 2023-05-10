from rest_framework import generics, permissions
from captured_drf_api.permissions import IsOwnerOrReadOnly
from .models import Tour
from .serializers import TourSerializer


class TourList(generics.ListCreateAPIView):
    """
    Lists tours and handles creation of a tour
    if logged in as an admin
    """
    serializer_class = TourSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        permissions.IsAdminUser
        ]
    queryset = Tour.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TourDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles editing and deleting of tours by id
    if the user is the owner
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = TourSerializer
    queryset = Tour.objects.all()
