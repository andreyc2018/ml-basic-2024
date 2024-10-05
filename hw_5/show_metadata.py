#!/usr/bin/env python
"""Create Mediafile object from a file.
   Show metadata attributes
"""

import argparse
from mediafiles.mediafiles import make_media_file

def main(filepath:str) -> None:
    print(f"Creating media object from file: {filepath}")
    media_object = make_media_file(filepath)
    print(f"Media object: {media_object}")
    print("Attributes:")
    attrs = media_object.list_attributes()
    for attr in attrs:
        print(f'  {attr} = {media_object.get_attribute(attr)}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser('show_metadata', 'show_metadata <filepath>')
    parser.add_argument('filepath', help='The file')
    args = parser.parse_args()
    try:
        main(args.filepath)
    except Exception as ex:
        print(ex)
