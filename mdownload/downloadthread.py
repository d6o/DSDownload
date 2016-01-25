#!/usr/bin/env python

"""
Diego Martins de Siqueira
MIT License
mdownload
"""

import threading
import os
import urllib

class downloadthread(threading.Thread):
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
            except Exception,e:
                print "   Error: %s"%e
            self._queue.task_done()

    def download_url(self, url):

        folder = self._destFolder

        if type(url) is dict:
            folder  = os.path.join(folder, url['folder'])
            url     = url['url']

        self._handlefolder(folder)

        name = url.split('/')[-1]

        if name == 'zip':
            name = url.split('/')[-2] + '.zip'

        dest = os.path.join(folder, name)
        print "[%s] Downloading %s"%(self.ident, name)
        urllib.urlretrieve(url, dest)