#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'yong'

import time, threading, thread
import requests
import logging
import os
from pbar import Bar

# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.INFO)

THREAD_LOC = threading.local()
logging.info("----")


def gainres(url, headers=None, num=3):
    """
    retry get response with {num} times
    """
    try:
        if not hasattr(THREAD_LOC, 'retry'): THREAD_LOC.retry = 1
        res = requests.get(url=url, headers=headers, stream=True)
        if res.status_code in (200, 206):
            logging.debug(" %s connected ." % url)
            return res
        else:
            logging.debug(" %s retry %s" % (url, THREAD_LOC.retry))
            if THREAD_LOC.retry < num:
                THREAD_LOC.retry += 1
                logging.debug(" %s retry %s" % (url, THREAD_LOC.retry))
                return gainres(url=url, headers=None, num=5)
            else:
                return res
    except Exception  as e:
        print e.message
        return None


def split(total, num, K=1000):
    """
    split total by num ranges ,lie [(0,9),(10,19),(20,30)]
    """
    chunk = total / K / num  # 每块大小(为K(1000)的整数倍)
    L = map(lambda x: (x * chunk * K, (x + 1) * chunk * K - 1), range(num - 1))
    L.insert(num, ((num - 1) * chunk * K, total))
    return L


def createFile(path, fName):
    if path and not os.path.isdir(path):
        os.makedirs(os.path.normpath(path))
    fullfName = path + os.sep + fName if path else fName
    if not os.path.isfile(fullfName):
        open(fullfName, 'wb').close()
        logging.info(" create file %s " % fullfName)


class Tracker(threading.Thread):
    def __init__(self, url, headers=None, path=None, fName=None, num=1):
        threading.Thread.__init__(self)
        self.url = url
        self.headers = headers
        self.path = path
        self.fName = fName if fName else url.split("/")[-1]
        self.num = num
        self.thread_pool = []
        self.total = 1
        self.current = 0

    def run(self):
        print "Tracker start ,waiting for connect ..."
        res = gainres(url=self.url, headers=self.headers)
        if res and res.status_code in (200, 206) and res.headers.__contains__('Content-Length'):
            print 'url--> %s  connected!' % self.url
            self.total = int(res.headers['Content-Length'])
            self.bar = Bar(title=self.fName, total=self.total, eta='ETA', currval=self.current)
            createFile(self.path, self.fName)
            L_ranges = split(self.total, self.num)
            self.thread_pool = map(lambda x: Worker(url=self.url, path=self.path, fName=self.fName, on_off=x), L_ranges)
            map(lambda t: t.start(), self.thread_pool)
            self.moniror()
            # map(lambda t: t.join(), self.thread_pool)
        else:
            print ' unsupport url %s  :%s ' % (self.url, res)

    def moniror(self):
        while self.current < self.total:
            speed, current = 0, 0
            for t in self.thread_pool:
                threadLock.acquire()
                speed += t.speed
                current += (t.current - t.on_off[0])
                self.current = current
                t.speed = 0
                threadLock.release()
            # progress = format(self.current / 1.0 / self.total, '.2%')
            # logging.debug('progress ----> %s   speed@%sk/s' % (progress, speed / 1024))
            self.bar.update(speed)
            time.sleep(1)


class Worker(threading.Thread):
    def __init__(self, url, headers=None, path=None, fName=None, on_off=None, curent=None):
        threading.Thread.__init__(self)
        self.url = url
        self.headers = headers if headers else {}
        self.path = path
        self.fName = fName if fName else url.split("/")[-1]
        self.on_off = on_off
        self.current = curent if curent else on_off[0]
        self.headers['Range'] = 'bytes=%s-%s' % self.on_off
        self.speed = 0  # 实时下载总量，父线程每秒对其清零

    def run(self):
        logging.info("Worker Starting  %s = %s" % (self, self.headers))
        res = gainres(url=self.url, headers=self.headers, num=5)
        if res and res.status_code in (200, 206):
            fullName = self.path + os.sep + self.fName if self.path else self.fName
            try:
                with  open(fullName, 'r+b') as file:
                    file.seek(self.current)
                    for chunk in res.iter_content(chunk_size=1024 * 1):
                        if chunk:
                            threadLock.acquire()
                            file.write(chunk)
                            file.flush()
                            self.speed += len(chunk)
                            self.current += len(chunk)
                            threadLock.release()
                            # logging.debug('%s ---> %s' % (threading.currentThread(), len(chunk)))
            except IOError as e:
                logging.error("file err " + e.args[1])
        else:
            logging.info(self.res)


threadLock = threading.Lock()
