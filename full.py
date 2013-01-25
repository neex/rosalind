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


def reverse_masses_get(x):
    return min(((j - x) ** 2, i) for (i, j) in masses)[1]


with open('rosalind_full.txt') as f:
    ps = map(float, filter(None, map(str.strip, f.readlines())))
    par = ps[0]
    ions = ps[1:]
    pair = []
    for i in xrange(len(ions)):
        pair.append(min(((ions[j] + ions[i] - par) ** 2, j) for j in xrange(len(ions)) if i != j)[1])
    used = [0] * len(ions)
    stack = [''] * len(ions)


    def canbe(s):
        for (j, k) in masses:
            if abs(k - s) < 0.00001:
                return j
        return None


    def rec(i, lastu):
        if i == len(ions):
            return True
        curs = ions[i] - ions[lastu]
        if i == lastu:
            used[i] = 1
            used[pair[i]] = 2
            return rec(i + 1, lastu)
        cb = canbe(curs)
        if used[i] == 1:
            if not cb:
                return False
            stack[i] = cb
            if rec(i + 1, i):
                return True
            stack[i] = ''
            return False
        if used[i] == 2:
            if rec(i + 1, lastu):
                return True
            return False
        if cb:
            used[i] = 1
            used[pair[i]] = 2
            stack[i] = cb
            if rec(i + 1, i):
                return True
            stack[i] = ''
            used[i] = 0
            used[pair[i]] = 0
        used[i] = 2
        used[pair[i]] = 1
        if rec(i + 1, lastu):
            return True
        used[i] = 1
        used[pair[i]] = 2
        return False


    rec(0, 0)
    print ''.join(stack)
