#!/usr/bin/env python

"""
Diego Martins de Siqueira
MIT License
mdownload - It is a small library to multi-threaded downloads.
"""

import Queue
import downloadthread
import sys
import argparse

def mdownload(urlList, workers = 5, folderPath = 'downloads'):
    queue = Queue.Queue()

    for url in urlList:
        queue.put(url)

    for i in range(workers):
        t = downloadthread.downloadthread(queue, folderPath)
        t.start()

    queue.join()

def main(argv):
    description =   "It is a small library to multi-threaded downloads."
    description +=  "This means that it can generate a queue and download several files simultaneously"
    parser = argparse.ArgumentParser(description = description)
    parser.add_argument("--threads", type=int, default=5, 
        help="Number of parallel downloads. The default is 5.")
    parser.add_argument("--output", type=str, default="downloads", 
        help="Output folder")
    parser.add_argument('urls', type=str, nargs='+',
        help='URLs to be downloaded')

    args = parser.parse_args()

    try:
        mdownload(args.urls, args.threads, args.output)
        print 'All files were downloaded.'
    except KeyboardInterrupt:
        print 'Interrupt received, stopping downloads'

    sys.exit()

if __name__ == "__main__":
   main(sys.argv[1:])