from rest_framework import serializers
from albums.models import Album

class AlbumSerializer(serializers.ModelSerializer):
    name = serializers.CharField(default="New Album")
    release_date = serializers.DateTimeField()
    cost = serializers.DecimalField(decimal_places = 3, max_digits=5)

    class Meta:
        model = Album
        fields = '__all__'


