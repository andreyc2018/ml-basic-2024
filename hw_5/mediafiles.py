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
        self.file_op = FileOps.instantiate(str(self.md.path), mode)
        return self

    def close(self) -> None:
        self.file_op.close()
        return self

    @abstractmethod
    def read(self) -> str:
        """Read file using """
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

    def __enter__(self):
        print('ENTER')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f'EXIT: {exc_type}, {exc_value}, {traceback}')

    def __eq__(self, other) -> bool:
        return self.md.media_type == other.md.media_type

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
    def __init__(self, mode:str):
        self.mode = mode

    @abstractmethod
    def read(self, file:MediaFile) -> str:
        pass

    @abstractmethod
    def write(self, file:MediaFile):
        pass

    @abstractmethod
    def close(self):
        pass

    @staticmethod
    def instantiate(path:str, mode:str):
        if path.startswith(CLOUD_PREFIX):
            return CloudFileOps(mode)
        return LocalFileOps(mode)


class LocalFileOps(FileOps):
    def __init__(self, mode:str) -> None:
        super().__init__(mode)

    def read(self, file:MediaFile) -> str:
        if MODE_READ not in self.mode:
            raise ValueError(f'Unable to read file {file.md.path} with mode {self.mode}')
        print('local read')
        return ''

    def write(self, file:MediaFile):
        if MODE_WRITE not in self.mode:
            raise ValueError(f'Unable to write file {file.md.path} with mode {self.mode}')
        print('local write')

    def close(self, file:MediaFile):
        print('local close')


class CloudFileOps(FileOps):
    def __init__(self) -> None:
        super().__init__()

    def read(self, file:MediaFile) -> str:
        if MODE_READ not in self.mode:
            raise ValueError(f'Unable to read file {file.md.path} with mode {self.mode}')
        print('cloud read')
        return ''

    def write(self, file:MediaFile):
        if MODE_WRITE not in self.mode:
            raise ValueError(f'Unable to write file {file.md.path} with mode {self.mode}')
        print('cloud write')

    def close(self, file:MediaFile):
        print('cloud close')


class AudioFile(MediaFile):
    def __init__(self, path:str) -> None:
        super().__init__(path, MEDIA_AUDIO)
        print(f'Create AuioFile {self.md.path}')

    def read(self) -> str:
        print(f'Read file {self.md.path}')
        return self.file_op.read(self)

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

    def read(self) -> str:
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

    def read(self) -> str:
        raise NotImplementedError

    def write(self) -> None:
        raise NotImplementedError

    def file_format(self) -> str:
        raise NotImplementedError

    def convert(self, fmt:str) -> None:
        raise NotImplementedError
