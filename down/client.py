#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'yong'

import sys
import getopt
from Tracker import Tracker


def Usage():
    print 'downloader usage:'
    print '-h,--help: print help message.'
    print '-v, --version: print script version'
    print '-u=,--url=example.com: url to be download .'
    print '-c=,--connection=n: connections (threads) will be opend to get the file .[default :1]'
    print '-d=,--dir=d:/file/xxx: the dir that download file will be saved in . [default:current dir]'
    print '-f=,-fName=xx: file name to be saved .[default:str after last ' / ']'


def Version():
    print 'PyTest.py 1.0.0'


def OutPut(args):
    print 'Hello, %s' % args


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hvu:c:d:f:',
                                   ['help', 'version', 'url=', 'connection=', 'dir=', 'fName='])
        url = None
        num = 1
        path = None
        fName = None
    except getopt.GetoptError, err:
        print str(err)
        Usage()
        sys.exit(2)
    for o, a in opts:
        if o in ('-h', '--help'):
            Usage()
            sys.exit(1)
        elif o in ('-v', '--version'):
            Version()
            sys.exit(0)
        elif o in ('-u', '--url'):
            url = a

        elif o in ('-c', '--connection'):
            num = int(a)
        elif o in ('-d', '--dir'):
            path = a
        elif o in ('-f', '--fName'):
            fName = a
        else:
            print 'unhandled option'
            sys.exit(3)

    tracker = Tracker(url=url, path=path, fName=fName, num=num)
    tracker.start()


if __name__ == '__main__':
    main()
