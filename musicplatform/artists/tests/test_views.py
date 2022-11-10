import pytest
import json
from artists.serilaizer import ArtistSerializer
from artists.models import Artist


@pytest.mark.django_db
def test_ArtistInvalidData(client):
    postingdata = {
        "stageName" : "artist1",
        "socialLink" : "http"
    }
    response = client.post('http://localhost:8000/artists/',postingdata)

    assert response.status_code == 400


@pytest.mark.django_db
def test_ArtistMissingData(client):
    postingdata = {
        "socialLink" : "http"
    }
    response = client.post('http://localhost:8000/artists/',postingdata)
    assert response.status_code == 400


