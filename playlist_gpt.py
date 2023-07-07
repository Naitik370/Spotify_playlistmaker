import spotipy
from spotipy.oauth2 import SpotifyOAuth
import openai
import spotifyauth

# Set up authentication
scope = "playlist-modify-private"  # Adjust the scope as needed
# Fetch the ChatGPT API key
chat_gpt_api_key = ''

# Set up the OpenAI API client
openai.api_key = chat_gpt_api_key

# Set up authentication for Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotifyauth.ID,client_secret=spotifyauth.secret,redirect_uri="http://localhost:8080/callback",scope=scope))

# Create a new playlist
playlist_name = ""
playlist_description = ""
user_id = sp.me()["id"]
playlist = sp.user_playlist_create(user_id, playlist_name, public=False, description=playlist_description)

# List of songs to add (replace with your own songs)
# Get song recommendations from ChatGPT
chat_prompt = "Give me a playlist for spotify songs. Give that in a python list"
response = openai.Completion.create(
    engine='davinci',
    prompt=chat_prompt,
    max_tokens=50,
)
song_list = response.choices[0].text.strip().split('\n')
print(song_list)

# Search and add songs to the playlist
for song in song_list:
    result = sp.search(q=song, type="track")
    if result["tracks"]["items"]:
        track_uri = result["tracks"]["items"][0]["uri"]
        sp.playlist_add_items(playlist["id"], [track_uri])
        print(song," added successfully")

print("Playlist created and songs added successfully!")
