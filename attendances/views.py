from rest_framework import generics, permissions
from captured_drf_api.permissions import IsOwnerOrReadOnly
from .models import Attendance
from .serializers import AttendanceSerializer


class AttendanceList(generics.ListCreateAPIView):
    """
    Lists attendances and handles creation of an
    attendance if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = AttendanceSerializer
    queryset = Attendance.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AttendanceDetail(generics.RetrieveDestroyAPIView):
    """
    Handles retrieving and deleting of attendances by id if owned
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AttendanceSerializer
    queryset = Attendance.objects.all()
