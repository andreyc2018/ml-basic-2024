from datetime import datetime
import os
from pathlib import Path
from typing import Self
from abc import ABC, abstractmethod

from .metadata import CLOUD_PREFIX


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
