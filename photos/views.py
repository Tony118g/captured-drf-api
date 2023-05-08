from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Photo
from .serializers import PhotoSerializer


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

