#!/usr/bin/python
# -*- coding: utf-8 -*-

from itertools import izip
with open('rosalind_kmer.txt') as f:
    f.readline().strip()
    s = ''.join(map(str.strip, f.readlines()))
    d = {}
    for x in map(''.join, izip(s, s[1:], s[2:], s[3:])):
        d[x] = d.get(x, 0) + 1
    alph = 'ACGT'
    for i in xrange(0, 4 ** 4):
        j = i
        tt = []
        for t in xrange(4):
            tt.append(alph[j % len(alph)])
            j /= len(alph)
        print d.get(''.join(tt[::-1]), 0),
    print

