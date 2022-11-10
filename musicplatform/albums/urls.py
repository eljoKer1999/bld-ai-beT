from django.urls import path
from albums.views import AlbumView,ManualAlbum

urlpatterns = [
    path("",AlbumView.as_view()),
    path("manual/",ManualAlbum.as_view())

]