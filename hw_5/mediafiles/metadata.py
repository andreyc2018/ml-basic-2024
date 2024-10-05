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
        self.name = location.split('/')[-1].split('.')[0]
        self.filesize = 0
        self.created = datetime.now()
        self.owner_id = os.getuid()
        self.format = self.location.suffix[1:]
        self._media_type = media_type


class AudioMetadata(Metadata):
    def __init__(self, path: str) -> None:
        super().__init__(path, MEDIA_AUDIO)
        self.format = "MP4A"
        self.rate = 48000
        self.channels = 32


class VideoMetadata(Metadata):
    def __init__(self, path: str) -> None:
        super().__init__(path, MEDIA_VIDEO)
        self.width = 1024
        self.height = 800
        self.codec = "H264"
        self.bitrate = 677

class ImageMetadata(Metadata):
    def __init__(self, path: str) -> None:
        super().__init__(path, MEDIA_IMAGE)
        self.width = 320
        self.height = 240
        self.ppi = 72
        self.colorspace = "RGB"
