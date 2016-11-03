#!/usr/bin/env python

"""
Diego Martins de Siqueira
MIT License
DSDownload - DSDownload is a fully featured download library with focus on performance
"""
import threading
import os
import logging
import queue as Queue
import urllib.request as urllib2


class DownloadThread(threading.Thread):
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

    def __init__(self, queue, dest_folder='downloads'):
        super(DownloadThread, self).__init__()

        self._queue = queue
        self._dest_folder = dest_folder
        self.daemon = True

        self._handle_folder(self._dest_folder)

    @staticmethod
    def _handle_folder(folder):
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
                logging.debug('Preparing to Download url:' + url)
                self.prepare_download(url)
                logging.debug('Download complete url:' + url)

            except Exception as e:
                logging.debug('Error downloading')
                print("Error: {0}".format(e))

            logging.debug('Task Done!')
            self._queue.task_done()

    def get_color(self, num):
        logging.debug('Getting Color')
        color_index = int(num) % len(self.colors)

        logging.debug('ColorIndex to Worker' + str(num) + ': ' + str(color_index))
        return self.colors[color_index]

    @staticmethod
    def get_file_name(headers, url):

        logging.debug('Getting Content Disposition')
        con_disposition = headers.get('Content-Disposition')

        if con_disposition:
            logging.debug('Content Disposition Found')
            logging.debug('Searching for filename')
            con_name = con_disposition.split('filename=')[-1].replace('"', '').replace(';', '')

            if con_name:
                logging.debug('Filename found: ' + con_name)
                return con_name

        logging.debug('Spliting URL for filename')
        file_name = url.split('/')[-1]
        logging.debug('Filename: ' + file_name)

        return file_name

    def prepare_download(self, url):

        wnum = threading.current_thread().name.split('-')[-1]
        logging.debug('Finding Worker number: ' + wnum)

        color = self.get_color(wnum)

        logging.debug('Opening connection')
        req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
        urlCon = urllib2.urlopen(req)

        logging.debug('Getting metadata')
        meta = url_con.info()

        file_name = self.get_file_name(meta, url)

        dest = os.path.join(self._dest_folder, file_name)
        logging.debug('Folder: ' + self._dest_folder)
        logging.debug('Destination: ' + dest)

        logging.debug('Opening file')
        dest_file = open(dest, 'wb')

        logging.debug('Getting file size')
        file_size = meta.get("Content-Length")
        logging.debug('File size:' + str(file_size))

        print(color + "Downloading: %s Bytes: %s" % (file_name, file_size) + self.color_reset)

        file_size = 0
        block_size = 8192
        logging.debug('Block size:' + str(block_size))

        while True:
            buffer = url_con.read(block_size)
            if not buffer:
                break

            logging.debug('Total Downloaded: ' + str(file_size))
            file_size += len(buffer)
            dest_file.write(buffer)

        logging.debug('Total Downloaded: ' + str(file_size))
        logging.debug('Closing file')
        dest_file.close()


def DSDownload(url_list, workers=5, folder_path='downloads'):
    logging.debug('Starting DSDownload')
    queue = Queue.Queue()
    logging.debug('Instantiating Queue')

    for url in url_list:
        logging.debug('Add url to Queue: ' + url)
        queue.put(url)

    logging.debug('Testing number of Workers')
    workers = workers if workers < len(url_list) else len(url_list)
    logging.debug('Workers:' + str(workers))

    for worker in range(workers):
        worker = str(worker + 1)
        logging.debug('Instantiating Worker: ' + worker)
        t = DownloadThread(queue, folder_path)
        logging.debug('Starting Worker: ' + worker)
        t.start()

    logging.debug('Waiting Workers')
    queue.join()
