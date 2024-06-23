#!/usr/bin/env python

from datetime import datetime
import os
from pathlib import Path

from abc import ABC, abstractmethod

CLOUD_PREFIX = 'https://'

MODE_READ = 'r'
MODE_WRITE = 'w'

MEDIA_AUDIO = 'audio'
MEDIA_VIDEO = 'video'
MEDIA_IMAGE = 'image'

MEDIATYPES = [MEDIA_AUDIO, MEDIA_IMAGE, MEDIA_VIDEO]

class Metadata(ABC):
    def __init__(self, path:str, media_type:str) -> None:
        self.path = Path(path)
        self.size = 0
        self.created = datetime.now()
        self.owner_id = os.getuid()
        self.format = self.path.suffix[1:]
        self.media_type = media_type


class MediaFile(ABC):
    def __init__(self, path:str, media_type:str) -> None:
        self.md = Metadata(path, media_type)
        self.buffer = ''
        self.file_op:FileOps = None

    def open(self, mode:str) -> None:
        self.file_op = FileOps.instantiate(self.md.path)

    @abstractmethod
    def read(self) -> None:
        pass

    @abstractmethod
    def write(self) -> None:
        pass

    @abstractmethod
    def file_format(self) -> str:
        pass

    @abstractmethod
    def convert(self, fmt:str) -> None:
        pass

    @property
    def media_type(self) -> str:
        return self.md.media_type

    @property
    def path(self) -> str:
        return str(self.md.path)

    def __eq__(self, other) -> bool:
        return self.md.media_type == other.md.medis_type

    @staticmethod
    def instantiate(path):
        ext = path.split('.')[-1]
        if ext == 'mp3':
            return AudioFile(path)
        elif ext == 'jpg':
            return ImageFile(path)
        elif ext == 'mpg':
            return VideoFile(path)
        raise ValueError(f"Unknown file type: {ext}")


class FileOps(ABC):
    @abstractmethod
    def read(self, file:MediaFile):
        pass

    @abstractmethod
    def write(self, file:MediaFile):
        pass

    @staticmethod
    def instantiate(path:str):
        if path.startswith(CLOUD_PREFIX):
            return CloudFileOps()
        return LocalFileOps()


class LocalFileOps(FileOps):
    def read(self, file:MediaFile):
        pass

    def write(self, file:MediaFile):
        pass


class CloudFileOps(FileOps):
    def read(self, file:MediaFile):
        pass

    def write(self, file:MediaFile):
        pass


class AudioFile(MediaFile):
    def __init__(self, path:str) -> None:
        super().__init__(path, MEDIA_AUDIO)
        print(f'Create AuioFile {self.md.path}')

    def read(self) -> None:
        print(f'Read file {self.md.path}')

    def file_format(self) -> str:
        print(f'File {self.md.path} format {self.md.format}')
        return self.md.format

    def convert(self, fmt:str) -> None:
        print(f'Convert file {self.md.path} from {self.md.format} to {fmt}')
        self.md.path = self.md.path.with_suffix(f'.{fmt}')
        print(self.md.path)

    def write(self) -> None:
        print(f'Write file {self.md.path}')


class VideoFile(MediaFile):
    def __init__(self, path:str) -> None:
        super().__init__(path, MEDIA_VIDEO)

    def read(self) -> None:
        raise NotImplementedError

    def write(self) -> None:
        raise NotImplementedError

    def file_format(self) -> str:
        raise NotImplementedError

    def convert(self, fmt: str) -> None:
        raise NotImplementedError


class ImageFile(MediaFile):
    def __init__(self, path:str) -> None:
        super().__init__(path, MEDIA_IMAGE)

    def read(self) -> None:
        raise NotImplementedError

    def write(self) -> None:
        raise NotImplementedError

    def file_format(self) -> str:
        raise NotImplementedError

    def convert(self, fmt:str) -> None:
        raise NotImplementedError


class FileReader:
    def __init__(self, file:MediaFile):
        self.file_op = FileOps.instantiate(file)
        self.

    def read(self, file:MediaFile):
        pass


def audio():
    audio = MediaFile.instantiate('./test_audio.mp3')
    try:
        file_op = LocalFileOps()
        reader = FileReader(file_op)
        reader.read(audio)
        audio.read()
        print(audio.file_format())
        audio.convert('wav')
    except Exception as ex:
        print(f'Error {ex}')


def main():
    audio()

if __name__ == '__main__':
    main()
