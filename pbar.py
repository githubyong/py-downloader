#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'yong'

import sys
import time
import datetime
import math
import random


class Bar:
    FORMAT = '%6.2f %s%s/s'
    PREFIXES = ' kMGTPEZY'

    def __init__(self, title, total, width=20, eta='ETA', currval=0, speed=0, fd=sys.stderr,
                 pchar=['', u"▏", u"▎", u"▍", u"▌", u"▋", u"▊", u"▉", u"█"], fillchar=' ', s_used=0):
        self.total = total
        self.title = title
        self.width = width
        self.eta = eta
        self.currval = currval
        self.speed = speed
        self.fd = fd
        self.pchar = pchar
        self.size_per_width = self.total / 1.0 / self.width  # datasize of per width [1/width]
        self.sub_size = self.size_per_width / len(self.pchar)  # sub data size of [1/pchar]
        self.bar = ''
        self.fillchar = fillchar
        self.s_used = s_used
        self.finished = False
        self.unit = 'B'

    def title_p(self):
        return '%s: %s' % (self.title, format(self.currval / 1.0 / self.total, '.2%'))

    def bar_p(self):
        completed = int(self.currval / self.size_per_width)
        if completed: self.bar = reduce(lambda x, y: x + y, map(lambda x: self.pchar[-1], range(completed)))
        percent_of_pchar = int((self.currval % self.size_per_width) / self.sub_size)  # tail
        return (str.join('', self.bar) + self.pchar[percent_of_pchar]).ljust(self.width, self.fillchar)

    def eta_p(self):
        if self.currval == 0 or not self.speed:
            return 'ETA:  --:--:--'
        elif self.finished:
            return 'Time: %s' % str(datetime.timedelta(seconds=int(self.s_used)))
        else:
            elapsed = (self.total - self.currval) / self.speed
            return 'ETA:  %s' % str(datetime.timedelta(seconds=int(elapsed)))

    def speed_p(self):
        power = int(math.log(self.speed, 1000)) if self.speed else 0
        scaled = self.speed / 1000. ** power
        return self.FORMAT % (scaled, self.PREFIXES[power], self.unit)

    def update(self, chunk):

        self.currval += chunk
        self.s_used += 1
        self.speed = chunk
        if self.currval >= self.total:
            self.finished = True
        self.fd.write('%s %s %s %s \r' % (self.title_p(), self.bar_p(), self.eta_p(), self.speed_p()))


def testbar():
    bar = Bar(title="xiami", total=1024 * 100, eta='ETA', currval=9.01, speed=8976)
    for i in range(50):
        bar.update(random.randint(1024 * 4, 1024 * 10))
        time.sleep(1)

# testbar()
