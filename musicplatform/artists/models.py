from django.db import models
from django.db.models import Count

class Artist(models.Model):
    stageName = models.CharField(unique=True, blank=False, max_length=70, null=False)
    socialLink = models.URLField(max_length=200, blank = True)

    def approved_albums(self):
     return self.album_set.filter(Approved=True).count()

    def __str__(self):
        return "Artist stageName is:" +self.stageName
    
    
    class Meta:
        db_table = 'artists'
        ordering = ['stageName']
