from artists.models import Artist
from albums.models import Album
from rest_framework import serializers

class ArtistSerializer(serializers.ModelSerializer):
    stageName = serializers.CharField()
    socialLink = serializers.URLField(required=False)

    class Meta:
        model = Artist
        fields = '__all__'


