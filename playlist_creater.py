import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotifyauth #My spotify key
# Set up authentication
scope = "playlist-modify-private"  # Adjust the scope as needed
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotifyauth.ID,client_secret=spotifyauth.secret,redirect_uri="http://localhost:8080/callback",scope=scope))

# Create a new playlist
playlist_name = "playlist"
playlist_description = "playlist desc"
user_id = sp.me()["id"]
playlist = sp.user_playlist_create(user_id, playlist_name, public=False, description=playlist_description)

# List of songs to add (replace with your own songs)
song_list = [
]



# Search and add songs to the playlist
for song in song_list:
    result = sp.search(q=song, type="track")
    if result["tracks"]["items"]:
        track_uri = result["tracks"]["items"][0]["uri"]
        sp.playlist_add_items(playlist["id"], [track_uri])

print("Playlist created and songs added successfully!")
