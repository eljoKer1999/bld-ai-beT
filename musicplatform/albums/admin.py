from django.contrib import admin
from albums.models import Album, Song

class InlineSong(admin.StackedInline):
      model = Song
      extra = 0
      min_num = 1

class AlbumAdmin(admin.ModelAdmin):
      inlines = [InlineSong]
      readonly_fields=('creation_date',)


admin.site.register(Album,AlbumAdmin)
admin.site.register(Song)
