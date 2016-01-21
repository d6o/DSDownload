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

        self._queue 		= queue
        self._destFolder 	= destFolder
        self.daemon         = True

        self._handlefolder()

    def _handlefolder(self):
        '''
            if folder does not exist, create it.
        '''

        if not os.path.exists(self._destFolder):
            os.makedirs(self._destFolder)

    def run(self):
        while True:
            url = self._queue.get()
            try:
                self.download_url(url)
            except Exception,e:
                print "   Error: %s"%e
            self._queue.task_done()

    def download_url(self, url):
    	name = url.split('/')[-1]
        dest = os.path.join(self._destFolder, name)
        print "[%s] Downloading %s"%(self.ident, name)
        urllib.urlretrieve(url, dest)