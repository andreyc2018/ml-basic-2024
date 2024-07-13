from abc import ABC, abstractmethod
from datetime import datetime
import os
from pathlib import Path

CLOUD_PREFIX = 'https://'

MEDIA_AUDIO = 'audio'
MEDIA_VIDEO = 'video'
MEDIA_IMAGE = 'image'

MEDIATYPES = [MEDIA_AUDIO, MEDIA_IMAGE, MEDIA_VIDEO]

class Metadata(ABC):
    def __init__(self, location:str, media_type:str) -> None:
        self.location = Path(location)
        self.name = ""
        self.filesize = 0
        self.created = datetime.now()
        self.owner_id = os.getuid()
        self.format = self.location.suffix[1:]
        self._media_type = media_type


class AudioMetadata(Metadata):
    def __init__(self, path: str) -> None:
        super().__init__(path, MEDIA_AUDIO)
        self.format = ''
        self.rate = 0
        self.channels = 0


class VideoMetadata(Metadata):
    def __init__(self, path: str) -> None:
        super().__init__(path, MEDIA_VIDEO)
        self.height = 0
        self.width = 0
        self.format = ""
        self.bitrate = 0

class ImageMetadata(Metadata):
    def __init__(self, path: str) -> None:
        super().__init__(path, MEDIA_IMAGE)
        self.height = 0
        self.width = 0
        self.ppi = ""
        self.colorspace = ""
