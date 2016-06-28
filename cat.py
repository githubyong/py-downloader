#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'yong'

import sys
import getopt
from Tracker import Tracker


def Usage():
    print u'''usage:
        -h,--help: 帮助.
        -v, --version: 版本信息.
        -u=,--url=下载文件的url.
        -c=,--connection=n:开启n个连接(线程)去下载文件.(默认:1，站点出口速度不好的话开多个可以加快下载速度).
        -d=,--dir=d:/file/xxx:保存文件的路径 (默认为当前文件夹).
        -f=,-fName=xx: 要保存的文件名(默认截取url的最后一个 '/'之后的字符串).
        eg:cat -u http://dlsw.baidu.com/sw-search-sp/soft/3d/20621/XMusicSetup_2_0_2_1618.1394071033.exe -c 3.'''



def Version():
    print 'PyTest.py 1.0.0'


def OutPut(args):
    print 'Hello, %s' % args


def main():
    try:
        shotopts = 'hvu:c:d:f:'
        longopts = ['help', 'version', 'url=', 'connection=', 'dir=', 'fName=']
        opts, args = getopt.getopt(sys.argv[1:], shotopts, longopts)
        if not sys.argv[1:]:
            Usage()
            sys.exit()
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
            print 'unhandled option !'
            Usage()
            sys.exit(3)

    tracker = Tracker(url=url, path=path, fName=fName, num=num)
    tracker.start()


if __name__ == '__main__':
    main()
