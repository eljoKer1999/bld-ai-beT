from django.contrib import admin
from albums.models import Album

class AlbumROmodel(admin.ModelAdmin):
      readonly_fields=('creation_date',)

admin.site.register(Album,AlbumROmodel)
