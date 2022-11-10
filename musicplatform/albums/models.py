from unicodedata import decimal
from django.db import models
from artists.models import Artist

class Album(models.Model):
    name = models.CharField(default="New Album", max_length=70)
    creation_date = models.DateTimeField(auto_now_add= True)
    release_date = models.DateTimeField()
    # DecimalField is suitable more than FloatField because
    # The float rounding issue Seth brings up is a problem for cost
    cost = models.DecimalField(decimal_places = 3, max_digits=5)
    Artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return "Album Name is:" + self.name


    class Meta:
        db_table = 'albums'
        ordering = ['creation_date']