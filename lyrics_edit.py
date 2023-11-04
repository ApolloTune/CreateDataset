import json
import os
from json.decoder import JSONDecodeError


def json_size(fileName):
    with open(fileName,'r', encoding='utf-8') as file:
        data = json.load(file)
    return len(data)

def remove_id_from_songs(fileName):
    with open(fileName,'r',encoding="utf-8") as file:
        data = json.load(file)
    for song in data:
        del song["id"]
    with open(fileName,'w',encoding='utf-8') as file2:
        json.dump(data, file2, ensure_ascii=False, indent=4)
    print('Dosyadaki id alani silindi...')

def add_id_from_songs(fileName):
    with open(fileName,'r',encoding="utf-8") as file:
        data = json.load(file)
    for i, song in enumerate(data, start=1):
        song["id"] = i
    with open(fileName, 'w', encoding="utf-8") as file2:
        json.dump(data, file2, ensure_ascii=False, indent=4)
    print('Dosyaya id alani eklendi...')

def non_duplicated_size(fileName):
    with open(fileName,'r',encoding="utf-8") as file:
        data = json.load(file)
    unique_song = {}
    for song in data:
        title = song["title"]
        if title not in unique_song:
            unique_song[title] = song
    return len(list(unique_song.values()))
def remove_duplicated_from_songs(fileName):
    with open(fileName,'r',encoding="utf-8") as file:
        data = json.load(file)
    unique_song = {}
    for song in data:
        title = song["title"]
        if title not in unique_song:
            unique_song[title] = song
    with open(fileName, 'w', encoding='utf-8') as file2:
        json.dump(list(unique_song.values()), file2, ensure_ascii=False, indent=4)
    print('Tekrar eden veriler silindi')

def filter_songs_with_title_in_lyrics(fileName):
    with open(fileName,'r', encoding="utf-8") as file:
        data = json.load(file)
    not_filtered_data = [song for song in data if song["title"].lower() not in song["lyrics"].lower()]
    filtered_data = [song for song in data if song["title"].lower() in song["lyrics"].lower()]
    print("Lyrics'i yanlış olan şarkı adeti: ",len(not_filtered_data))
    with open(fileName,'w', encoding='utf-8') as file2:
        json.dump(filtered_data, file2, ensure_ascii=False, indent=4)
    print("Lyrics'i bozuk olan şarkılar silindi...")


print("Şarkı adeti:",json_size("sarki_sozleri.json"))
# remove_id_from_songs("sarki_sozleri.json")
print("Tekrar Etmeyen Şarkı Adeti: ",non_duplicated_size("sarki_sozleri.json"))
# remove_duplicated_from_songs("sarki_sozleri.json")
# filter_songs_with_title_in_lyrics("sarki_sozleri.json")
# add_id_from_songs("sarki_sozleri.json")