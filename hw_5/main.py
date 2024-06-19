#!/usr/bin/env python

from datetime import datetime
import os

from abc import ABC, abstractmethod

FILEFORMAT = []

class Metadata(ABC):
    def __init__(self, path:str) -> None:
        self.path = path
        self.size = 0
        self.created = datetime.now()
        self.owner_id = os.getuid()
        self.format = path.split('.')[-1]


class MediaFile(ABC):
    def __init__(self, path:str) -> None:
        self.md = Metadata(path)
        self.buffer = ''

    @abstractmethod
    def read(self) -> None:
        pass

    @abstractmethod
    def write(self) -> None:
        pass

    @abstractmethod
    def file_format(self) -> None:
        pass

    @abstractmethod
    def convert(self) -> None:
        pass


class FileOps(ABC):
    @abstractmethod
    def read(self, file:MediaFile):
        """Read file specified in MediaFile::md::path
           to MediaFile::buffer"""
        pass

    @abstractmethod
    def write(self, file:MediaFile):
        pass


class LocalFileOps(ABC):
    def read(self, file:MediaFile):
        pass

    def write(self, file:MediaFile):
        pass


class CloudFileOps(ABC):
    def read(self, file:MediaFile):
        pass

    def write(self, file:MediaFile):
        pass


class AudioFile(MediaFile):
    def __init__(self, path:str) -> None:
        super().__init__(path)
        print(f'Create AuioFile {self.md.path}')

    def read(self) -> None:
        print(f'Read file {self.md.path}')

    def file_format(self) -> None:
        print(f'File {self.md.path} format {self.md.format}')

    def convert(self, fmt:str) -> None:
        print(f'Convert file {self.md.path} from {self.md.format} to {fmt}')
        print(self.md.path.split('.')[:-1])


class VideoFile(MediaFile):
    def __init__(self, path:str) -> None:
        super().__init__(path)


class ImageFile(MediaFile):
    def __init__(self, path:str) -> None:
        super().__init__(path)


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
