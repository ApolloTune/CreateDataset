import json
import re

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

def clean_lyrics(lyrics):
    cleaned_lyrics = re.sub(r'\[.*?\]', '', lyrics)
    return cleaned_lyrics.strip()
def remove_lyrics_header(lyrics):
    lyrics = lyrics.strip()

    start = lyrics.find("Lyrics")
    if start != -1:
        end = lyrics.find("\n", start)
        if end != -1:
            lyrics = lyrics[end + 1:]

    return lyrics.strip()

def clean_lyrics_in_json(fileName):
    with open(fileName, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for song in data:
        song['lyrics'] = clean_lyrics(song['lyrics'])
        song['lyrics'] = remove_lyrics_header(song['lyrics'])
        song['lyrics'] = song['lyrics'].replace('\n', '')

    with open(fileName, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print("Sarki Sozleri Duzenlendi")

filename = input("Lutfen dosyanizin ismini giriniz: ")
print("Şarkı adeti:",json_size(filename))
remove_id_from_songs(filename)
# print("Tekrar Etmeyen Şarkı Adeti: ", non_duplicated_size(filename))
# remove_duplicated_from_songs(filename)
# filter_songs_with_title_in_lyrics(filename)
# clean_lyrics_in_json(filename)
add_id_from_songs(filename)
