import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotifyauth #My spotify key
# Set up authentication
scope = "playlist-modify-private"  # Adjust the scope as needed
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotifyauth.ID,client_secret=spotifyauth.secret,redirect_uri="http://localhost:8080/callback",scope=scope))

# Create a new playlist
playlist_name = "Eng Pop"
playlist_description = "A curated playlist for intense workouts"
user_id = sp.me()["id"]
playlist = sp.user_playlist_create(user_id, playlist_name, public=False, description=playlist_description)

# List of songs to add (replace with your own songs)
song_list = [
    "Wake Me Up - Avicii",
    "Closer - The Chainsmokers ft. Halsey",
    "Without You - Avicii ft. Sandro Cavazza",
    "Don't Let Me Down - The Chainsmokers ft. Daya",
    "Hey Brother - Avicii",
    "Something Just Like This - The Chainsmokers ft. Coldplay",
    "Levels - Avicii",
    "Roses - The Chainsmokers ft. ROZES",
    "Waiting for Love - Avicii",
    "Paris - The Chainsmokers",
    "Shape of You - Ed Sheeran",
    "Bad Guy - Billie Eilish",
    "Can't Stop the Feeling! - Justin Timberlake",
    "Love Yourself - Justin Bieber",
    "Dance Monkey - Tones and I",
    "Uptown Funk - Mark Ronson ft. Bruno Mars",
    "Happy - Pharrell Williams",
    "Shake It Off - Taylor Swift",
    "Havana - Camila Cabello ft. Young Thug",
    "Blinding Lights - The Weeknd",
    "Watermelon Sugar - Harry Styles",
    "Memories - Maroon 5",
    "Don't Start Now - Dua Lipa",
    "Someone You Loved - Lewis Capaldi",
    "Castle on the Hill - Ed Sheeran",
]



# Search and add songs to the playlist
for song in song_list:
    result = sp.search(q=song, type="track")
    if result["tracks"]["items"]:
        track_uri = result["tracks"]["items"][0]["uri"]
        sp.playlist_add_items(playlist["id"], [track_uri])

print("Playlist created and songs added successfully!")
