#!/usr/bin/python
# -*- coding: utf-8 -*-

with open('rosalind_lexf.txt') as f:
    alph = f.readline().strip().split()
    k = int(f.readline().strip())
    for i in xrange(0, len(alph) ** k):
        j = i
        tt = []
        for t in xrange(k):
            tt.append(alph[j % len(alph)])
            j /= len(alph)
        print ''.join(tt[::-1])

