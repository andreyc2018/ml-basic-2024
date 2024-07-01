#!/usr/bin/env python

from datetime import datetime
import os
from pathlib import Path
from typing import Self

from abc import ABC, abstractmethod

CLOUD_PREFIX = 'https://'

MEDIA_AUDIO = 'audio'
MEDIA_VIDEO = 'video'
MEDIA_IMAGE = 'image'

MEDIATYPES = [MEDIA_AUDIO, MEDIA_IMAGE, MEDIA_VIDEO]

class Metadata(ABC):
    def __init__(self, location:str, media_type:str) -> None:
        self.location = Path(location)
        self.size = 0
        self.created = datetime.now()
        self.owner_id = os.getuid()
        self.format = self.location.suffix[1:]
        self.media_type = media_type


class AudioMetadata(Metadata):
    def __init__(self, path: str) -> None:
        super().__init__(path, MEDIA_AUDIO)
        self.title = ''
        self.artist = ''


class VideoMetadata(Metadata):
    def __init__(self, path: str) -> None:
        super().__init__(path, MEDIA_VIDEO)
        self.title = ''
        self.director = ''


class ImageMetadata(Metadata):
    def __init__(self, path: str) -> None:
        super().__init__(path, MEDIA_IMAGE)
        self.height = 0
        self.width = 0


class MediaFile(ABC):
    def __init__(self, metadata:Metadata) -> None:
        self.md = metadata
        self.data = ''
        self.file_op = FileOps.make(str(self.md.location))

    def load(self) -> bool:
        """Load the file"""
        print(f"Load the file {self.md.location}")
        with self.file_op.open(str(self.md.location)) as f:
            self.data = self.file_op.read()
        return True

    @abstractmethod
    def write(self) -> None:
        pass

    @abstractmethod
    def save(self) -> None:
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
        return str(self.md.location)

    def copy(self, other:Self):
        print('ASSIGN')
        self.data = other.data
        return self

    def same_type(self, other) -> bool:
        return self.md.media_type == other.md.media_type

    @staticmethod
    def make(path:str):
        ext = path.split('.')[-1]
        if ext == 'mp3':
            return AudioFile(path)
        elif ext == 'jpg':
            return ImageFile(path)
        elif ext == 'mpg':
            return VideoFile(path)
        raise ValueError(f"File {path}: unknown type: {ext}")


class FileOps(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def open(self, file:str) -> Self:
        pass

    @abstractmethod
    def read(self) -> str:
        pass

    @abstractmethod
    def write(self, data:str):
        pass

    @abstractmethod
    def close(self):
        pass

    def __enter__(self):
        print('ENTER')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f'EXIT: {exc_type}, {exc_value}, {traceback}')

    @staticmethod
    def make(path:str):
        if path.startswith(CLOUD_PREFIX):
            return CloudFileOps()
        return LocalFileOps()


class LocalFileOps(FileOps):
    def __init__(self) -> None:
        super().__init__()

    def open(self, file:str) -> Self:
        return self

    def read(self) -> str:
        print('local read')
        return ''

    def write(self, file:str):
        print('local write')

    def close(self):
        print('local close')


class CloudFileOps(FileOps):
    def __init__(self) -> None:
        super().__init__()

    def read(self) -> str:
        print('cloud read')
        return ''

    def write(self, data:str):
        print('cloud write')

    def close(self):
        print('cloud close')

    def open(self, file: str) -> Self:
        raise NotImplementedError


class AudioFile(MediaFile):
    def __init__(self, path:str) -> None:
        super().__init__(AudioMetadata(path))
        print(f'Create AuioFile {self.md.location}')

    def file_format(self) -> str:
        print(f'File {self.md.location} format {self.md.format}')
        return self.md.format

    def convert(self, fmt:str) -> None:
        print(f'Convert file {self.md.location} from {self.md.format} to {fmt}')
        self.md.location = self.md.location.with_suffix(f'.{fmt}')
        print(self.md.location)

    def write(self) -> None:
        print(f'Write file {self.md.location}')

    def save(self) -> None:
        print(f'Save file {self.md.location}')
        with self.file_op.open(str(self.md.location)) as f:
            f.write(self.data)


class VideoFile(MediaFile):
    def __init__(self, path:str) -> None:
        super().__init__(VideoMetadata(path))

    def write(self) -> None:
        raise NotImplementedError

    def file_format(self) -> str:
        raise NotImplementedError

    def convert(self, fmt: str) -> None:
        raise NotImplementedError

    def save(self) -> None:
        raise NotImplementedError


class ImageFile(MediaFile):
    def __init__(self, path:str) -> None:
        super().__init__(ImageMetadata(path))

    def write(self) -> None:
        raise NotImplementedError

    def file_format(self) -> str:
        raise NotImplementedError

    def convert(self, fmt:str) -> None:
        raise NotImplementedError

    def save(self) -> None:
        raise NotImplementedError
