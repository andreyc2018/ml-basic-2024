#!/usr/bin/env python
"""Copy media file using mediafiles module."""

import argparse
from mediafiles.mediafiles import MediaFile, make_media_file

def main(src:str, dst:str) -> None:
    src_file = make_media_file(src)
    dst_file = make_media_file(dst)
    if not src_file.same_type(dst_file):
        raise ValueError(f'Unable to copy {src_file.media_type} file {src} to {dst_file.media_type} file {dst}')
    src_file.load()
    dst_file.copy(src_file)
    dst_file.save()


if __name__ == '__main__':
    parser = argparse.ArgumentParser('copy', 'copy <source> <destination>')
    parser.add_argument('src', help='Source file')
    parser.add_argument('dst', help='Destination file')
    args = parser.parse_args()
    try:
        main(args.src, args.dst)
    except Exception as ex:
        print(ex)
