from django.contrib import admin
from artists.models import Artist
from albums.models import Album

class albumAdmin(admin.StackedInline):
    model = Album
    extra = 1 

class aritstAdmin(admin.ModelAdmin):
    inlines = [albumAdmin]
    list_display=['stageName','approved_albums']
    def get_name(self, obj):
        return obj.Artist.stageName

admin.site.register(Artist, aritstAdmin)
