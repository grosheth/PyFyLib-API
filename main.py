import spotipy, dotenv, os, sys
from spotipy.oauth2 import SpotifyClientCredentials

from typing import Union
from fastapi import FastAPI
from tools.authentication import *
from tools.artists import *

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/top10")
def get_top10():
    lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

    spotify = login()
    results = spotify.artist_top_tracks(lz_uri)

    for track in results['tracks'][:10]:
        print('track    : ' + track['name'])
        print('audio    : ' + track['preview_url'])
        print('cover art: ' + track['album']['images'][0]['url'])
        print()

    return {"top10"}

@app.get("/song")
def get_song(): 
    get_artist_id(artist="hugo", track="coma")
    return {"albums"}

