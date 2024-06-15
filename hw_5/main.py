#!/usr/bin/env python

import datetime

FILEFORMAT = []

class Metadata:
    def __init__(self) -> None:
        self.name = ''
        self.size = 0
        self.created = datetime.datetime
        self.owner_id = 0
        self.format = ''

class AudioMetadata(Metadata):
    def __init__(self) -> None:
        super().__init__()

class VideoMetadata(Metadata):
    def __init__(self) -> None:
        super().__init__()

class ImageMetadata(Metadata):
    def __init__(self) -> None:
        super().__init__()

class File:
    def __init__(self, path) -> None:
        self.path = path

class MediaFile:
    def __init__(self) -> None:
        self.metadata = None

class Directory(File):
    def __init__(self, path) -> None:
        super().__init__(path)

class AudioFile(MediaFile):
    def __init__(self) -> None:
        super().__init__()
        self.metadata = AudioMetadata()

class VideoFile(MediaFile):
    def __init__(self) -> None:
        super().__init__()
        self.metadata = VideoMetadata()

class ImageFile(MediaFile):
    def __init__(self) -> None:
        super().__init__()
        self.metadata = ImageMetadata()


def main():
    audio = AudioFile('./test_audio.mp3')
    try:
        audio.read()
        audio.file_type()
        audio.convert()
    except Exception as ex:
        print(f'Error {ex}')
