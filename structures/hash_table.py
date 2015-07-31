# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class HashTable(object):

    def __init__(self, size):
        self.table_list = [[] for x in xrange(size)]
