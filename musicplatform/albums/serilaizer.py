from rest_framework import serializers
from albums.models import Album
from artists.models import Artist


class ArtistSerializerInner(serializers.ModelSerializer):
    stageName = serializers.CharField()
    socialLink = serializers.URLField(required=False)

    class Meta:
        model = Artist
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    name = serializers.CharField(default="New Album")
    release_date = serializers.DateTimeField()
    cost = serializers.DecimalField(decimal_places = 3, max_digits=5)
    Approved = serializers.BooleanField(default=False)
    artist = ArtistSerializerInner()

    class Meta:
        model = Album
        fields = '__all__'


class PostAlbumSerializer(serializers.ModelSerializer):
    name = serializers.CharField(default = "New Album")
    release_datetime = serializers.DateTimeField()
    cost = serializers.DecimalField(decimal_places = 3, max_digits=5)
    Approved = serializers.BooleanField(default=False)

    class Meta:
        model = Album
        fields = '__all__'