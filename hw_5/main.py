#!/usr/bin/env python

import datetime

from abc import ABC, abstractmethod

FILEFORMAT = []

class Metadata(ABC):
    def __init__(self, path:str) -> None:
        self.path = path
        self.size = 0
        self.created = datetime.datetime
        self.owner_id = 0
        self.format = path.split('.')[-1]


class AudioMetadata(Metadata):
    def __init__(self, path:str) -> None:
        super().__init__(path)


class VideoMetadata(Metadata):
    def __init__(self, path:str) -> None:
        super().__init__(path)


class ImageMetadata(Metadata):
    def __init__(self, path:str) -> None:
        super().__init__(path)


class MediaConverter(ABC):
    @abstractmethod
    def run(self, media):
        pass


class AudioConverter(MediaConverter):
    pass


class MediaFile(ABC):
    def __init__(self, meta, path:str) -> None:
        self.md = meta(path)
        self.buffer = ''

    @abstractmethod
    def read(self) -> None:
        pass

    @abstractmethod
    def file_format(self) -> None:
        pass

    @abstractmethod
    def convert(self) -> None:
        pass


class AudioFile(MediaFile):
    def __init__(self, path:str) -> None:
        super().__init__(AudioMetadata, path)
        print(f'Create AuioFile {self.md.path}')

    def read(self) -> None:
        print(f'Read file {self.md.path}')

    def file_format(self) -> None:
        print(f'File {self.md.path} format {self.md.format}')

    def convert(self, fmt:str) -> None:
        print(f'Convert file {self.md.path} from {self.md.format} to {fmt}')
        print(self.md.path.split('.')[:-1])
        converter = AudioConverter()
        converter.run(self)


class VideoFile(MediaFile):
    def __init__(self, path:str) -> None:
        super().__init__(VideoMetadata, path)


class ImageFile(MediaFile):
    def __init__(self, path:str) -> None:
        super().__init__(ImageMetadata, path)


def audio():
    audio = AudioFile('./test_audio.mp3')
    try:
        audio.read()
        audio.file_format()
        audio.convert('wav')
    except Exception as ex:
        print(f'Error {ex}')


def main():
    audio()

if __name__ == '__main__':
    main()
