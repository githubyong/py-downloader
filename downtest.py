#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'yong'
from Tracker import Tracker

xiami = 'http://dlsw.baidu.com/sw-search-sp/soft/3d/20621/XMusicSetup_2_0_2_1618.1394071033.exe'
vbox = 'https://atlas.hashicorp.com/puphpet/boxes/centos65-x64/versions/20151130/providers/virtualbox.box'
landen='https://raw.githubusercontent.com/getlantern/lantern-binaries/master/lantern-installer.exe'
tracker = Tracker(vbox, num=6)
tracker.start()