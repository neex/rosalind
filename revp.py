#!/usr/bin/python
# -*- coding: utf-8 -*-

with open('rosalind_revp.txt') as f:
    ss = f.readline().strip()

counted = {}
rev = dict(zip('ACGT', 'TGCA'))


def count(x, y):
    if x > y:
        return True
    if (x, y) in counted:
        return counted[(x, y)]
    counted[(x, y)] = rev[ss[x]] == ss[y] and count(x + 1, y - 1)
    return counted[(x, y)]


for i in xrange(len(ss)):
    for j in xrange(i + 3, len(ss)):
        if count(i, j):
            print i + 1, j - i + 1
