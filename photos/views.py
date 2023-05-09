from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Photo
from .serializers import PhotoSerializer
from captured_drf_api.permissions import IsOwnerOrReadOnly


class PhotoList(APIView):
    serializer_class = PhotoSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        photos = Photo.objects.all()
        serializer = PhotoSerializer(
            photos, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = PhotoSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class PhotoDetail(APIView):
    """
    Handles retrieving, updating and deleting photos
    """
    serializer_class = PhotoSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        """
        Gets a photo by id
        """
        try:
            photo = Photo.objects.get(pk=pk)
            self.check_object_permissions(self.request, photo)
            return photo
        except Photo.DoesNotExist:
            raise Http404

    def get(self, request, pk):

        photo = self.get_object(pk)
        serializer = PhotoSerializer(
            photo,
            context={'request': request}
            )
        return Response(serializer.data)
