from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from artists.models import Artist
from .serilaizer import ArtistSerializer

class ArtistView(APIView):
    def get(self, request):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)

    def post(self, request):
        serilaizer = ArtistSerializer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response ({"message" : "Artist Created"}, status=status.HTTP_201_CREATED)

        return Response (serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)

    
