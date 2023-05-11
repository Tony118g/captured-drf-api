from rest_framework import generics, permissions
from captured_drf_api.permissions import IsOwnerOrReadOnly
from .models import Photo
from .serializers import PhotoSerializer


class PhotoList(generics.ListCreateAPIView):
    """
    Lists photos and handles creation of a photo if logged in
    """

    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Photo.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating and deleting photos by id if owned
    """
    serializer_class = PhotoSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Photo.objects.all()
