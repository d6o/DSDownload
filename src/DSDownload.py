#!/usr/bin/env python

"""
Diego Martins de Siqueira
MIT License
DSDownload - DSDownload is a fully featured download library with focus on performance
"""
import sys

if sys.version_info[0] == 2:
    import Queue
else:
    import queue as Queue

import downloadthread

def DSDownload(urlList, workers = 5, folderPath = 'downloads'):
    queue = Queue.Queue()

    for url in urlList:
        queue.put(url)

    for worker in range(workers):
        t = downloadthread.downloadthread(queue, folderPath)
        t.start()

    queue.join()
