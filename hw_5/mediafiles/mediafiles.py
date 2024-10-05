from datetime import datetime
from typing import Self, Union, List
from abc import ABC, abstractmethod

from . import metadata as md
from .fileops import FileOps


def detect_file_type(filename:str) -> str:
    ext = filename.split('.')[-1]
    if ext == 'mp3':
        return md.MEDIA_AUDIO
    if ext == 'mpg':
        return md.MEDIA_VIDEO
    if ext == 'jpg':
        return md.MEDIA_IMAGE
    return 'unknown'


class MediaFile(ABC):
    def __init__(self, metadata:md.Metadata) -> None:
        self.md = metadata
        self.data = ''
        self.file_op = FileOps.make(str(self.md.location))

    def load(self) -> bool:
        """Load the file"""
        print(f"Load {self.md._media_type} file {self.md.location}")
        with self.file_op.open(str(self.md.location)) as f:
            self.data = self.file_op.read()
        return True

    def list_attributes(self) -> List[str]:
        attrs = [attr for attr in self.md.__dict__.keys() if not attr.startswith('_')]
        return attrs

    def get_attribute(self, attr:str):
        return self.md.__dict__[attr]

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
        return self.md._media_type

    @property
    def path(self) -> str:
        return str(self.md.location)

    def __str__(self) -> str:
        return f"{self.md.location}: {self.media_type}"


class AudioFile(MediaFile):
    def __init__(self, path:str) -> None:
        super().__init__(md.AudioMetadata(path))

    def file_format(self) -> str:
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
        super().__init__(md.VideoMetadata(path))

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
        super().__init__(md.ImageMetadata(path))

    def write(self) -> None:
        raise NotImplementedError

    def file_format(self) -> str:
        raise NotImplementedError

    def convert(self, fmt:str) -> None:
        raise NotImplementedError

    def save(self) -> None:
        raise NotImplementedError


def make_media_file(path:str) -> Union[AudioFile, ImageFile, VideoFile]:
    kind = detect_file_type(path.split('/')[-1])
    if kind == md.MEDIA_AUDIO:
        return AudioFile(path)
    elif kind == md.MEDIA_IMAGE:
        return ImageFile(path)
    elif kind == md.MEDIA_VIDEO:
        return VideoFile(path)
    raise ValueError(f"File {path}: unknown media type: {kind}")
