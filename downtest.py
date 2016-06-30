#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'yong'
from Tracker import Tracker

xiami = 'http://dlsw.baidu.com/sw-search-sp/soft/3d/20621/XMusicSetup_2_0_2_1618.1394071033.exe'
vbox = 'https://atlas.hashicorp.com/puphpet/boxes/centos65-x64/versions/20151130/providers/virtualbox.box'
landen='https://raw.githubusercontent.com/getlantern/lantern-binaries/master/lantern-installer.exe'
mysql='http://124.202.164.12/files/21550000086CE8B0/120.52.73.12/cdn.mysql.com//Downloads/MySQL-5.6/mysql-5.6.31-win32.zip'
tracker = Tracker(vbox, num=6)
tracker.start()