#!/usr/bin/python
# -*- coding: utf-8 -*-


class Node:

    def __init__(self, par):
        self.p = par
        self.s = set()
        self.lab = ''

    def __repr__(self):
        return '%s(s=%s)' % (self.lab or 'Node', self.s)


def buildtree(tree):

    class cur:

        pos = 0

    dd = {}

    def getnode(par):
        cc = Node(par)
        if tree[cur.pos] == '(':
            while tree[cur.pos] in '(,':
                cur.pos += 1
                cc.s.add(getnode(cc))
            cur.pos += 1
        ff = cur.pos
        while tree[cur.pos] not in '), ;':
            cur.pos += 1
        nam = tree[ff:cur.pos]
        cc.lab = nam
        if nam != '':
            dd[nam] = cc
        return cc

    return (getnode(None), dd)


from itertools import chain


def dist(x, y, ng):
    if x == y:
        return 0
    for i in chain(x.s, (x.p, )):
        if i != ng:
            c = dist(i, y, x)
            if c != -1:
                return c + 1
    return -1


with open('rosalind_nwck.txt') as f:
    ss = filter(None, map(str.strip, f.readlines()))
    for (s1, s2) in zip(ss[::2], ss[1::2]):
        tree = s1
        (v1, v2) = s2.split()
        (root, d) = buildtree(tree)
        print dist(d[v1], d[v2], None),
print
