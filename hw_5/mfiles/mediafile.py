from typing import Optional

class MediaFileReader:
    def __init__(self):
        self.mf:Optional[MediaFile] = None

    def read(self, loc:str) -> bytes:
        with open(loc, mode='rb') as f:
            return f.read()


class MediaFileWriter:
    def __init__(self):
        self.mf:Optional[MediaFile] = None

    def write(self, loc:str, data:Optional[bytes]):
        assert data is not None
        with open(loc, mode='wb') as f:
            f.write(data)


class MediafileMetadata:
    def __init__(self):
        self.loc = ""
        self.owner_uid = 0
        self.data:Optional[bytes] = None
        self.mf:Optional[MediaFile] = None


class MediaFile:
    def __init__(self, md:MediafileMetadata, wr:MediaFileWriter, rd:MediaFileReader):
        self.md = md
        md.mf = self

        self.wr = wr
        wr.mf = self

        self.rd = rd
        rd.mf = self

    def read(self, fname:str):
        self.md.loc = fname
        self.md.data = self.rd.read(self.md.loc)

    def write(self, fname:str):
        self.md.loc = fname
        self.wr.write(self.md.loc, self.md.data)
