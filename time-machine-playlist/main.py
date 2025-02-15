import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
CLIENT_ID = "a0f36c098ec0435ea92efd0bbd94351b"
CLIENT_SECRET = "afddeef62c6e40669f8c2ceacb82daca"
REDIRECT_URL = "https://hazzmattx.com/spotify-playlist"
# Billboard Top 100 request
date = input("Which day would you like to travel to? Type it in as YYYY-MM-DD.\n")
year = date.split("-")[0]
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
url  = "https://www.billboard.com/charts/hot-100/" + date
response = requests.get(url=url, headers=header)
response.raise_for_status()
song_urls = []
soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
# Spotipy search
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                              client_secret=CLIENT_SECRET,
                              redirect_uri=REDIRECT_URL,
                              scope="playlist-modify-private",
                              cache_path=".cache"))
user_id = sp.current_user()["id"]
for song in song_names:
    try:
        query = f"track:{song} year:{year}"
        result = sp.search(q=query, type="track", limit=1)
        track_uri = result["tracks"]["items"][0]["uri"]
        song_urls.append(track_uri)
    except IndexError:
        print(f"Could not find {song} on Spotify. Skipping...")
# Create the playlist
playlist_name = f"{date} Billboard 100"
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, collaborative=False)
playlist_id = playlist["id"]
print(f"Created playlist: {playlist_name} (ID: {playlist_id})")
sp.playlist_add_items(playlist_id=playlist_id, items=song_urls)
