from rest_framework import generics, permissions
from captured_drf_api.permissions import IsOwnerOrReadOnly
from .models import Tour
from .serializers import TourSerializer


class TourList(generics.ListCreateAPIView):
    """
    Lists tours or create a tour if logged in.
    """
    serializer_class = TourSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        permissions.IsAdminUser
        ]
    queryset = Tour.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
