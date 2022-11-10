from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from albums.models import Album
from .serilaizer import AlbumSerializer

class AlbumView(APIView):
    def get(self, request):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)

    def post(self, request):
        serilaizer = AlbumSerializer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response ({"message" : "Album Created"}, status=status.HTTP_201_CREATED)

        return Response (serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)


