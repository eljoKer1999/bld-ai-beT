from rest_framework import status
from albums.models import Album
from rest_framework.response import Response
from .serilaizer import AlbumSerializer,PostAlbumSerializer
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from knox.auth import TokenAuthentication
from django_filters import rest_framework
from musicplatform.permissions import IsTheUserArtistOrReadOnly,IsAuthenticatedUserorReadOnly
from .filters import FilteringAlbum
from django import forms
from rest_framework.pagination import LimitOffsetPagination

# class AlbumView(APIView):
#    def get(self, request):
#        albums = Album.objects.all()
#        serializer = AlbumSerializer(albums, many=True)
#        return Response(serializer.data)

#    def post(self, request):
#        serilaizer = AlbumSerializer(data=request.data)
#        if serilaizer.is_valid():
#            serilaizer.save()
#            return Response ({"message" : "Album Created"}, status=status.HTTP_201_CREATED)

#       return Response (serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlbumView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsTheUserArtistOrReadOnly&IsAuthenticatedUserorReadOnly]
    queryset = Album.objects.filter(Approved=True)
    serializer_class = AlbumSerializer
    filter_backends = (rest_framework.DjangoFilterBackend)
    filterset_class = FilteringAlbum
    filterset_fields = ('cost','name')
    
    
    def post(self, request):
        serilaizer = AlbumSerializer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response ({"message" : "Album Created"}, status=status.HTTP_201_CREATED)

        return Response (serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)

class ManualAlbum(APIView):
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticatedUserorReadOnly]

    def get(self, request, format=None):
        lte = request.query_params.get('lte')
        gte = request.query_params.get('gte')
        name = request.query_params.get('name')
        try:
            if(not lte is None):
                lte = int(lte)
        except:
            raise forms.ValidationError("lte's wrong data type")
        try:
            if(not gte is None):
                gte = int(gte)
        except:
            raise forms.ValidationError("gte's wrond data type")
        albums = Album.objects.filter(Approved = True)

        if(not gte is None):
            albums = albums.filter(cost_greaterthanOrEqual = gte).all()

        if( not lte is None):
            albums = albums.filter(cost_LessthanOrEqual = lte).all()  

        if(not name is None):
            albums = albums.filter(name__icontains= name).all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)

