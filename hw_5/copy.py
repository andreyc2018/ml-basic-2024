#!/usr/bin/env python
"""Copy media file using mediafiles module."""

import argparse
import mediafiles

def main(src:str, dst:str) -> None:
    src_file = mediafiles.MediaFile.make(src)
    dst_file = mediafiles.MediaFile.make(dst)
    if src_file != dst_file:
        raise ValueError(f'Unable to copy {src_file.media_type} file {src} to {dst_file.media_type} file {dst}')
    with (src_file.open('r') as s, dst_file.open('w') as d):
        while buffer := s.read():
            d.write(buffer)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('copy', 'copy <source> <destination>')
    parser.add_argument('src', help='Source file')
    parser.add_argument('dst', help='Destination file')
    args = parser.parse_args()
    try:
        main(args.src, args.dst)
    except Exception as ex:
        print(ex)
