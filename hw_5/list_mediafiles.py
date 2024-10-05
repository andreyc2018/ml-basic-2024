#!/usr/bin/env python
"""Iterate files in a directory
   Create media objects and show metadata attributes
"""

import argparse
import os
from mediafiles.mediafiles import make_media_file

def show_metadata(filepath:str) -> None:
    try:
        media_object = make_media_file(filepath)
    except ValueError:
        return
    print(f"Media object: {media_object}")
    print("Attributes:")
    attrs = media_object.list_attributes()
    for attr in attrs:
        print(f'  {attr} = {media_object.get_attribute(attr)}')

def main(dir:str) -> None:
    print(f"List media files in {dir}")
    for subdir, dirs, files in os.walk(dir):
        for file in files:
            show_metadata(os.path.join(subdir, file))


if __name__ == '__main__':
    parser = argparse.ArgumentParser('list_mediafiles', 'list_mediafiles <dir>')
    parser.add_argument('dir', help='A dir with media files')
    args = parser.parse_args()
    try:
        main(args.dir)
    except Exception as ex:
        print(ex)
