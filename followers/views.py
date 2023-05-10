from django.shortcuts import render
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from rest_framework import generics, permissions
from .models import Follower
from .serializers import FollowerSerializer
from captured_drf_api.permissions import IsOwnerOrReadOnly


class FollowerList(generics.ListCreateAPIView):
    """
    Lists followers and handles creation of a follower if logged in.
    """
    serializer_class = FollowerSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
        ]
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Handles retrieving and deleting of followers by id if owned
    """
    serializer_class = FollowerSerializer
    permission_classes = [
        IsOwnerOrReadOnly
        ]
    queryset = Follower.objects.all()
