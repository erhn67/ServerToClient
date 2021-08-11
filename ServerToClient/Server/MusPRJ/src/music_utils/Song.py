import os,sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)
from os import listdir
from os.path import isfile, join

from typing import List

from src.utils import Constants


class Song:
    def __init__(self, file=''):
        self.file_name = file

    def get(self):
        file = open(self.file_name, 'rb')
        self.file_name
        song_bytes = file.read()
        print(len(song_bytes))
        file.close()
        return song_bytes


def get_songs(path: str) -> List[Song]:
    try:
        temp = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith('mp3')]
        songs = []
        for s in temp:
            songs.append(Song(os.path.join(Constants.PATH_TO_MUSIC_LIB, s)))
    except FileNotFoundError as err:
        print(err)
        return []
    return songs


def to_string(songs: List[Song]) -> str:
    s = ""
    index = 1
    for song in songs:
        s += "[{}] ~ {}\n".format(index, song.file_name.replace(Constants.PATH_TO_MUSIC_LIB, ""))
        index += 1
    return s
