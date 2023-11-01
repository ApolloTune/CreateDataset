import os
import json
import spotipy
import lyricsgenius as lg
import spotipy.util as util
from json.decoder import JSONDecodeError
from dotenv import load_dotenv
load_dotenv()
scope = "playlist-read-private"
spotifyOAuth = spotipy.SpotifyOAuth(client_id=os.getenv('SPOTIPY_CLIENT_ID'),
                                    client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
                                    redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
                                    scope=scope)
token = spotifyOAuth.get_cached_token()
spotifyObject = spotipy.Spotify(auth=token['access_token'])
genius_access_token = os.getenv('GENIUS_ACCESS_TOKEN')
genius = lg.Genius(genius_access_token)
i=1
sarki_listesi = []
while True:
    playlist_class = input("Lutfen Playlistinizin Sinifini Giriniz (Mutlu-Ask-Enerjik-Huzunlu): ") 
    playlist_link = input("Lutfen Spotify'dan çekmek istediğiniz playlist'in bağlantısını giriniz: ")
    playlist_id = playlist_link.split('/')[-1].split('?')[0]
    results = spotifyObject.playlist_tracks(playlist_id)
    for item in results["items"]:
        track = item['track']
        title = track['name']
        artist = ', '.join([artist['name'] for artist in track['artists']])
        song = genius.search_song(title=title, artist=artist)
        try:
            lyrics = song.lyrics
            sarki_listesi.append({
                "id":i,
                "title": title,
                "artist": artist,
                "lyrics": lyrics,
                "class":playlist_class
            })
            print()
            print(f"{i}. sarki sozleri: {lyrics}")
            print()
            i = i + 1
        except:
            print()
            print(">> lyrics were not found")
            print()
    devam_et = input("Başka bir playlist çekmek istiyor musunuz? (E/H): ")
    if devam_et.lower() != 'e':
        break
with open("sarki_sozleri.json", "a", encoding="utf-8") as json_dosyasi:
    json.dump(sarki_listesi, json_dosyasi, indent=4, ensure_ascii=False)
print("Veri JSON dosyasına yazıldı: sarki_sozleri.json")
