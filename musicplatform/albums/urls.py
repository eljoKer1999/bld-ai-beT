from django.urls import path
from albums.views import AlbumView

urlpatterns = [
    path("",AlbumView.as_view())
]