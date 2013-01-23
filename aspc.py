#!/usr/bin/python
# -*- coding: utf-8 -*-

with open('rosalind_aspc.txt') as f:
    (n, m) = map(int, f.readline().strip().split())
    dd = [0]
    for nn in xrange(1, n + 1):
        d = []
        for k in xrange(0, nn + 1):
            if k == 0:
                d.append(1)
            elif k == nn:
                d.append(1)
            else:
                d.append((dd[k - 1] + dd[k]) % 1000000)
        dd = d
    print sum(d[k] for k in xrange(m, n + 1)) % 1000000
