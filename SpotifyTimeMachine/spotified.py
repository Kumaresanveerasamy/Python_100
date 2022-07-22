import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id="783489af76994e368a4740d2650d79f8",
        client_secret="f0549aea6a704eea8d1988b15df4331e",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

songs_uri = []

with open("playlist_2020-01-01.txt") as file:
    songs = file.readlines()

for song in songs:
    result = sp.search(q=f"track: {song}", type="track")

    try:
        songs_uri.append( result["tracks"]["items"][0]["uri"])

    except IndexError:
        print(f"{song} doesn't exist in spotify..")

print(songs_uri)

playlist = sp.user_playlist_create(user=user_id, name=" Top 100 Billboard of your Time..", public=False)
sp.playlist_add_items(playlist_id=playlist['id'], items=songs_uri)
