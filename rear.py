#!/usr/bin/python
# -*- coding: utf-8 -*-

import collections


def allvar(p1):
    for i in xrange(len(p1)):
        for j in xrange(i + 2, len(p1) + 1):
            yield p1[:i] + p1[i:j][::-1] + p1[j:]


def calc(p1, p2):
    if p1 == p2:
        return 0
    target = tuple(p2)
    fromfirst = {tuple(p1): 0}
    q = collections.deque((p1, ))
    while len(q):
        s = q.popleft()
        c = fromfirst[s]
        for j in allvar(s):
            if j == target:
                return c + 1
            if not j in fromfirst:
                fromfirst[j] = c + 1
                if c != 4:
                    q.append(j)
    fromsecond = {tuple(p2): 0}
    target = tuple(p1)
    q = collections.deque((p2, ))
    anss = 100000
    while len(q):
        s = q.popleft()
        c = fromsecond[s]
        if c == 4:
            break
        for j in allvar(s):
            if j == target:
                return c + 1
            if not j in fromsecond:
                fromsecond[j] = c + 1
                if c != 3:
                    q.append(j)
            if j in fromfirst:
                anss = min(anss, fromfirst[j] + fromsecond[j])
    return anss


with open('rosalind_rear.txt') as f:
    ss = map(str.strip, f.readlines())
ress = []
for i in xrange(0, len(ss), 3):
    f = tuple(map(int, ss[i].split()))
    t = tuple(map(int, ss[i + 1].split()))
    ress.append(calc(t, f))
print ' '.join(map(str, ress))
