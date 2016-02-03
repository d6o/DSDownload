#!/usr/bin/env python

"""
Diego Martins de Siqueira
MIT License
DSDownload - DSDownload is a fully featured download library with focus on performance
"""

import sys
import argparse
import logging
from DSDownload import DSDownload

def main(argv=sys.argv[0]):
    description =   "DSDownload is a fully featured download library with focus on performance"
    parser = argparse.ArgumentParser(
        description = description)
    parser.add_argument("--version", action="version", version='1.6.0.1',
        help="Version Info")
    parser.add_argument("--workers", type=int, default=5, 
        help="Number of parallel downloads. The default is 5.")
    parser.add_argument("--output", type=str, default="downloads", 
        help="Output folder")
    parser.add_argument('urls', type=str, nargs='+',
        help='URLs to be downloaded')
    parser.add_argument("-v", "--verbose", action="store_true",
        help="increase output verbosity")

    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    download = DSDownload
    if type(sys) is type(DSDownload):
        download = DSDownload.DSDownload
    try:
        DSDownload(args.urls, args.workers, args.output)
        print('All files were downloaded.')
    except KeyboardInterrupt:
        print('Interrupt received, stopping downloads')

    sys.exit()

if __name__ == "__main__":
   main(sys.argv[1:])
