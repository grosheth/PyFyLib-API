import os, spotipy, dotenv
from spotipy.oauth2 import SpotifyClientCredentials

dotenv.load_dotenv()

def login():
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(os.getenv("SPOTIPY_CLIENT_ID"), os.getenv("SPOTIPY_CLIENT_SECRET")))
    return spotify
