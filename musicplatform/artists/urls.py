from django.urls import path
from artists.views import ArtistView

urlpatterns = [
    path("",ArtistView.as_view())
]