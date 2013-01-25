#!/usr/bin/python
# -*- coding: utf-8 -*-

nodes = []


class Node:

    idd = 0

    def __init__(self, par):
        self.p = par
        self.s = set()
        self.lab = ''
        self.slcnt = 0
        self.qhere = 0
        Node.idd += 1
        self.idd = Node.idd
        nodes.append(self)

    def __repr__(self):
        return '%s(slcnt=%s, qhere=%s, s=%s)' % (self.lab or 'Node' + str(self.idd), self.slcnt, self.qhere, self.s)


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
        cc.s = tuple(cc.s)
        ff = cur.pos
        while tree[cur.pos] not in '), ;':
            cur.pos += 1
        nam = tree[ff:cur.pos]
        cc.lab = nam
        if nam != '':
            dd[nam] = cc
        return cc

    return (getnode(None), dd)


def cnt(cur):
    print cur
    cur.slcnt = 0
    for son in cur.s:
        cur.slcnt += cnt(son)
    if cur.lab:
        cur.slcnt += 1
    if cur.s:
        cur.qhere = cur.s[0].slcnt * cur.s[1].slcnt + (cur.slcnt - 1) * ((1 if cur.lab else 0))
    return cur.slcnt


with open('rosalind_cntq.txt') as f:
    n = int(f.readline().strip())
    (root, d) = buildtree(f.readline().strip())
    cnt(root)
    print root
