#!/usr/bin/python
# -*- coding: utf-8 -*-

masses = dict((
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

with open('rosalind_prsm.txt') as f:
    n = int(f.readline().strip())
    prots = [f.readline().strip() for i in xrange(n)]
    fts = map(float, f.readlines())
    overallmax = -1
    overallans = ''
    for s in prots:
        fs = [sum(map(masses.get, s[:i])) for i in xrange(len(s) + 1)] + [sum(map(masses.get, s[i:])) for i in xrange(len(s) + 1)]
        ll = sorted(i - j for i in fts for j in fs)
        mxc = 0
        mxr = 0
        t = 0
        prev = -100000000000.0
        for i in ll:
            if i - prev > 0.0000001:
                t = 0
            t += 1
            prev = i
            if mxc < t:
                mxc = t
                mxr = i

        if mxc > overallmax:
            overallmax = mxc
            overallans = s
    print overallmax
    print overallans
