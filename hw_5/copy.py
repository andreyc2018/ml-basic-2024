#!/usr/bin/env python
"""Copy media file using mediafiles module """

import argparse
import mediafiles

def main(srd:str, dst:str) -> None:
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser('copy', 'copy <source> <destination>')
    parser.add_argument('src', help='Source file')
    parser.add_argument('dst', help='Destination file')
    args = parser.parse_args()
    try:
        main(args.src, args.dst)
    except Exception as ex:
        print(ex)
