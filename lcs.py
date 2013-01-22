#!/usr/bin/python
# -*- coding: utf-8 -*-

import collections


class Node:

    def __init__(self):
        self.s = {}
        self.mark = 0

    def __repr__(self):
        return 'Node (mark=%s, d=%s)' % (self.mark, self.s)


with open('rosalind_lcs.txt') as f:
    strs = filter(None, map(str.strip, f.readlines()))
root = Node()
root.mark = len(strs)
for (mark, s) in enumerate(strs, 1):
    for i in xrange(len(s)):
        cur = root
        for c in s[i:]:
            if not c in cur.s:
                cur.s[c] = Node()
            cur = cur.s[c]
            if cur.mark >= mark - 1:
                cur.mark = mark
            else:
                break
stack = [''] * len(strs[0])
bestres = ''


def findbest(t, l):
    global bestres, stack
    if t.mark != len(strs):
        return
    if l > len(bestres):
        bestres = ''.join(stack)
    for x in t.s:
        stack[l + 1] = x
        findbest(t.s[x], l + 1)
        stack[l + 1] = ''


findbest(root, 0)
print bestres
