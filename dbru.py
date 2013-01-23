#!/usr/bin/python
# -*- coding: utf-8 -*-

import string
with open('rosalind_dbru.txt') as f:
    lines = map(str.strip, f.readlines())
    dd = set()
    for i in lines:
        dd.add((i[:-1], i[1:]))
        l = i.translate(string.maketrans('ACGT', 'TGCA'))[::-1]
        dd.add((l[:-1], l[1:]))
    for (x, y) in sorted(dd):
        print '(%s, %s)' % (x, y)
