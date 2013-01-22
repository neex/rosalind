#!/usr/bin/python
# -*- coding: utf-8 -*-

import collections


def allvar(p1):
    for i in xrange(len(p1)):
        for j in xrange(i + 2, len(p1) + 1):
            yield (p1[:i] + p1[i:j][::-1] + p1[j:], (i + 1, j))


def calc(p1, p2):
    if p1 == p2:
        return 0
    target = tuple(p2)
    fromfirst = {tuple(p1): 0}
    histfromfirst = {tuple(p1): ()}
    q = collections.deque((p1, ))
    while len(q):
        s = q.popleft()
        c = fromfirst[s]
        hist = histfromfirst[s]
        for (j, zz) in allvar(s):
            if j == target:
                return (c + 1, hist + (zz, ))
            if not j in fromfirst:
                fromfirst[j] = c + 1
                histfromfirst[j] = hist + (zz, )
                if c != 4:
                    q.append(j)
    fromsecond = {tuple(p2): 0}
    histfromsecond = {tuple(p2): ()}
    target = tuple(p1)
    q = collections.deque((p2, ))
    anss = 100000
    anshist = ()
    while len(q):
        s = q.popleft()
        c = fromsecond[s]
        hist = histfromsecond[s]
        for (j, zz) in allvar(s):
            if not j in fromsecond:
                fromsecond[j] = c + 1
                histfromsecond[j] = hist + (zz, )
                if c != 3:
                    q.append(j)
            if j in fromfirst:
                if anss > fromfirst[j] + fromsecond[j]:
                    anss = fromfirst[j] + fromsecond[j]
                    anshist = histfromfirst[j] + histfromsecond[j][::-1]
    return (anss, anshist)


with open('rosalind_sort.txt') as f:
    ff = tuple(map(int, f.readline().split()))
    tt = tuple(map(int, f.readline().split()))
    (r1, r2) = calc(ff, tt)
    print r1
    for (x1, x2) in r2:
        print x1, x2
