from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app, getAlbumByArtist, getMusicsByArtist, getEverything, getArtists, getAlbumImage, getAlbumPrice

client = TestClient(app)
    
def test_get_album_by_artist():
    response = client.get("/{nom_artiste}")
    assert type("{nom_artiste}") == str
    assert response.status_code == 200
    assert response.json() == {"Artiste": "{nom_artiste}", 'Albums': getAlbumByArtist("{nom_artiste}")}

def test_get_musics_by_artist():
    response = client.get("/{nom_artiste}/{nom_album}")
    assert type("{nom_artiste}") == str
    assert type("{nom_album}") == str
    assert response.status_code == 200
    assert response.json() == {"Artiste": "{nom_artiste}", 'Musiques': getMusicsByArtist("{nom_artiste}","{nom_album)}"), 'Image': getAlbumImage("{nom_artiste}","{nom_album}"), 'Prix': getAlbumPrice("{nom_artiste}","{nom_album}")}

def test_get_everything():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Item": getEverything()}