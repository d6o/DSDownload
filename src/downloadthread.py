#!/usr/bin/env python

"""
Diego Martins de Siqueira
MIT License
DSDownload - DSDownload is a fully featured download library with focus on performance
"""
import sys

if sys.version_info[0] == 2:
    import urllib
else:
    import urllib.request as urllib
import threading
import os
    
class downloadthread(threading.Thread):

    colors = [
        '\033[91m',
        '\033[92m',
        '\033[94m',
        '\033[96m',
        '\033[97m',
        '\033[93m',
        '\033[95m',
        '\033[90m',
        '\033[90m',
        '\033[99m',
    ]

    color_reset = '\033[0m'

    def __init__(self, queue, destFolder = 'downloads'):
        super(downloadthread, self).__init__()

        self._queue         = queue
        self._destFolder    = destFolder
        self.daemon         = True

        self._handlefolder(self._destFolder)

    def _handlefolder(self, folder):
        '''
            if folder does not exist, create it.
        '''

        if not os.path.exists(folder):
            os.makedirs(folder)

    def run(self):
        while True:
            url = self._queue.get()
            try:
                self.download_url(url)
            except Exception as e:
                print("Error: {0}".format(e))
            self._queue.task_done()

    def getColor(self,num):

        num = int(num) % len(self.colors)

        return self.colors[num]

    def download_url(self, url):

        folder = self._destFolder

        if type(url) is dict:
            folder = os.path.join(folder, url['folder'])
            url = url['url']

        self._handlefolder(folder)

        name = url.split('/')[-1]

        if name == 'zip':
            name = url.split('/')[-2] + '.zip'

        dest = os.path.join(folder, name)
        wnum = threading.current_thread().name.split('-')[-1]
        print(self.getColor(wnum) + "[Worker " + wnum + "] Downloading " + name + self.color_reset)
        urllib.urlretrieve(url, dest)
