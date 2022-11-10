from artists.models import Artist
from rest_framework import serializers

class ArtistSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    stageName = serializers.CharField(max_length = 70, allow_blank = False)
    socialLink = serializers.URLField(required=True , allow_blank = True)

    def stageNameValidator(self, value):
        if Artist.objects.filter(stageName__exact=value).exists():
            raise serializers.ValidationError("Name is already in use!")
        return value

    def create(self, validatedData):
        """
        Given the approved data, create a new instance of "Artist" and return it.
        """
        return Artist.objects.create(**validatedData)

    def update(self, instance , validatedData):
        """
        Given the approved data, update and return an existing instance of "Artist".
        """
        instance.stageName = validatedData.get('stageName',instance.stageName)
        instance.socialLink = validatedData.get('socialLink',instance.socialLink)
        instance.save()
        return instance
        
    class Meta:
        model = Artist
        fields = '__all__'


