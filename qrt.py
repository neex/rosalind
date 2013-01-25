#!/usr/bin/python
# -*- coding: utf-8 -*-

from itertools import product

with open('rosalind_qrt.txt') as f:
    names = f.readline().strip().split()
    resres = set()
    for s in f:
        nol = [i for (n, i) in enumerate(names) if s[n] == '0']
        edi = [i for (n, i) in enumerate(names) if s[n] == '1']
        nolpairs = ((nol[i], nol[j]) for i in xrange(len(nol)) for j in xrange(i + 1, len(nol)))
        edipairs = ((edi[i], edi[j]) for i in xrange(len(edi)) for j in xrange(i + 1, len(edi)))
        for c in product(nolpairs, edipairs):
            resres.add(frozenset(map(frozenset, c)))
    for ((a, b), (c, d)) in resres:
        print '{%s, %s} {%s, %s}' % (a, b, c, d)

