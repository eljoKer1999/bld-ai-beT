from email.policy import default
from django.db import models
from artists.models import Artist
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.core.exceptions import ValidationError
from django import forms
import os

class Album(models.Model):
    name = models.CharField(default="New Album", max_length=70)
    creation_date = models.DateTimeField(auto_now_add= True)
    release_date = models.DateTimeField()
    # DecimalField is suitable more than FloatField because
    # The float rounding issue Seth brings up is a problem for cost
    cost = models.DecimalField(decimal_places = 3, max_digits=5)
    Artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    # Album is approved by an admin or not
    Approved = models.BooleanField(default=False, help_text="If the album's name doesn't contain inappropriate expressions, approve it.")

    def __str__(self):
        return "Album Name is:" + self.name

    class Meta:
        db_table = 'albums'
        ordering = ['creation_date']

def fileExtensionValidator(value):
    extent = os.path.splitext(value.name)[1]
    validExtensions = ['.wav', '.mp3']
    if not extent.lower() in validExtensions:
        raise ValidationError('Unsupported file extension.')

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, default = "")
    name = models.CharField(blank= True, max_length=70)
    image = models.ImageField(blank=False, null=False)
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(100, 50)],
                                     format='JPEG',
                                     options={'quality': 60})
    audio = models.FileField(upload_to='musics/',blank=False, null=False, default='New Song',
                            help_text=("Allowed type - .mp3, .wav,"),validators=[fileExtensionValidator])

    def __str__(self):
        return self.name + " Song, in " + self.album.name + " Album "

    def clean(self):
        if self.name == "":
            self.name = self.album.name

    def delete(self, *args, **kwargs): 
        if (self.album.song_set.all().count()>1):
            super(Song, self).delete(*args, **kwargs)
        else:
            raise forms.ValidationError("Can't be deleted")

    class Meta:
        db_table = 'songs'