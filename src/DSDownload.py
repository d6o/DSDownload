#!/usr/bin/env python

"""
Diego Martins de Siqueira
MIT License
DSDownload - DSDownload is a fully featured download library with focus on performance
"""
import sys

if sys.version_info[0] == 2:
    import Queue
    import urllib2
else:
    import queue as Queue
    import urllib.request as urllib2

import threading
import os
import logging
    
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

    colorReset = '\033[0m'

    def __init__(self, queue, destFolder = 'downloads'):
        super(downloadthread, self).__init__()

        self._queue         = queue
        self._destFolder    = destFolder
        self.daemon         = True

        self._handlefolder(self._destFolder)

    def _handlefolder(self, folder):
        logging.debug('Testing Folder: ' + folder)
        if not os.path.exists(folder):
            logging.debug('Folder not found')
            logging.debug('Creating Folder: ' + folder)
            os.makedirs(folder)

    def run(self):

        while True:
            logging.debug('Getting URL from Queue')
            url = self._queue.get()
            logging.debug('URL:' + url)

            try:
                logging.debug('Preparing to Download url:'+ url)
                self.prepareDownload(url)
                logging.debug('Download complete url:'+ url)

            except Exception as e:
                logging.debug('Error downloading')
                print("Error: {0}".format(e))

            logging.debug('Task Done!')
            self._queue.task_done()

    def getColor(self,num):
        logging.debug('Getting Color')
        colorIndex = int(num) % len(self.colors)

        logging.debug('ColorIndex to Worker' + str(num) + ': '+ str(colorIndex))
        return self.colors[colorIndex]

    def getFileName(self, headers, url):

        logging.debug('Getting Content Disposition')
        conDisposition = headers.get('Content-Disposition')

        if conDisposition:
            logging.debug('Content Disposition Found')
            logging.debug('Searching for filename')
            conName = conDisposition.split('filename=')[-1].replace('"','').replace(';','')

            if conName:
                logging.debug('Filename found: '+conName)
                return conName

        logging.debug('Spliting URL for filename')
        fileName = url.split('/')[-1]
        logging.debug('Filename: ' + fileName)

        return fileName


    def prepareDownload(self, url):

        wnum = threading.current_thread().name.split('-')[-1]
        logging.debug('Finding Worker number: ' + wnum)

        color = self.getColor(wnum)

        logging.debug('Opening connection')
        urlCon = urllib2.urlopen(url)

        logging.debug('Getting metadata')
        meta = urlCon.info()

        fileName = self.getFileName(meta, url)

        dest = os.path.join(self._destFolder, fileName)
        logging.debug('Folder: ' + self._destFolder)
        logging.debug('Destination: ' + dest)

        logging.debug('Opening file')
        destFile = open(dest, 'wb')


        logging.debug('Getting file size')
        fileSize = meta.get("Content-Length")
        logging.debug('File size:' + str(fileSize))

        print(color + "Downloading: %s Bytes: %s" % (fileName, fileSize) + self.colorReset)

        fileSizeDL = 0
        blockSize = 8192
        logging.debug('Block size:' + str(blockSize))

        while True:
            buffer = urlCon.read(blockSize)
            if not buffer:
                break

            logging.debug('Total Downloaded: ' + str(fileSizeDL))
            fileSizeDL += len(buffer)
            destFile.write(buffer)

        logging.debug('Total Downloaded: ' + str(fileSizeDL))
        logging.debug('Closing file')
        destFile.close()

def DSDownload(urlList, workers = 5, folderPath = 'downloads'):
    logging.debug('Starting DSDownload')
    queue = Queue.Queue()
    logging.debug('Instantiating Queue')

    for url in urlList:
        logging.debug('Add url to Queue: ' + url)
        queue.put(url)

    logging.debug('Testing number of Workers')
    workers = workers if workers < len(urlList) else len(urlList)
    logging.debug('Workers:'+str(workers))

    for worker in range(workers):
        worker = str(worker + 1)
        logging.debug('Instantiating Worker: ' + worker)
        t = downloadthread(queue, folderPath)
        logging.debug('Starting Worker: ' + worker)
        t.start()

    logging.debug('Waiting Workers')
    queue.join()
