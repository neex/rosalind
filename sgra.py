#!/usr/bin/python
# -*- coding: utf-8 -*-

masses = list((
    ('A', 71.03711),
    ('C', 103.00919),
    ('D', 115.02694),
    ('E', 129.04259),
    ('F', 147.06841),
    ('G', 57.02146),
    ('H', 137.05891),
    ('I', 113.08406),
    ('K', 128.09496),
    ('L', 113.08406),
    ('M', 131.04049),
    ('N', 114.04293),
    ('P', 97.05276),
    ('Q', 128.05858),
    ('R', 156.10111),
    ('S', 87.03203),
    ('T', 101.04768),
    ('V', 99.06841),
    ('W', 186.07931),
    ('Y', 163.06333),
    ))

with open('rosalind_sgra.txt') as f:
    ps = sorted(map(float, filter(None, map(str.strip, f.readlines()))))
    n = len(ps)


    def canbe(s):
        for (j, k) in masses:
            if abs(k - s) < 0.01:
                return j
        return None


    anss = [None] * n
    for i in xrange(n - 1, -1, -1):
        anss[i] = (0, '')
        for j in xrange(i + 1, n):
            cc = canbe(ps[j] - ps[i])
            if cc:
                rs = anss[j][0] + 1
                if rs > anss[i][0]:
                    anss[i] = (rs, cc + anss[j][1])
    print ''.join(max(anss)[1])
