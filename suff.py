#!/usr/bin/python
# -*- coding: utf-8 -*-

import collections


class Node:

    def __init__(self):
        self.s = {}

    def __repr__(self):
        return 'Node (d=%s)' % self.s


with open('rosalind_suff.txt') as f:
    s = f.readline().strip()
root = Node()
for i in xrange(len(s)):
    cur = root
    for c in s[i:]:
        if not c in cur.s:
            cur.s[c] = Node()
        cur = cur.s[c]


def ptr(t, l):
    if len(t.s) == 1:
        for x in t.s:
            l.append(x)
            ptr(t.s[x], l)
    else:
        if l:
            print ''.join(l)
        for x in t.s:
            ptr(t.s[x], [x])


ptr(root, None)
