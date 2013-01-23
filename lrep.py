#!/usr/bin/python
# -*- coding: utf-8 -*-

import collections


class node:

    def __init__(self, lab):
        self.f = self.t = 0
        self.s = set()
        self.lab = lab

    def __repr__(self):
        return '%s(f=%s, t=%s, s=%s)' % tuple(map(str, (self.lab, self.f, self.t, self.s)))


sons = set()
with open('rosalind_lrep.txt') as f:
    sss = f.readline().strip()
    k = int(f.readline().strip())
    d = {}
    for x in map(str.strip, f.readlines()):
        (p, s, loc, ln) = x.split()
        (loc, ln) = map(int, (loc, ln))
        pnod = d.setdefault(p, node(p))
        snod = d.setdefault(s, node(s))
        snod.f = loc - 1
        snod.t = loc + ln - 1
        pnod.s.add(snod)
        sons.add(snod)
    root = (set(d.values()) - sons).pop()
bestlen = 0
bestst = []
st = []


def find(r, l):
    global bestlen, bestst
    ss = 0
    if r.t == len(sss):
        return 1
    st.append((r.f, r.t))
    for son in r.s:
        ss += find(son, l + r.t - r.f)
    if ss >= k and l + r.t - r.f > bestlen:
        bestst = list(st)
        bestlen = l + r.t - r.f
    st.pop()
    return ss


find(root, 0)
print ''.join(sss[i:j] for (i, j) in bestst)
