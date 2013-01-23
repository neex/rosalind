#!/usr/bin/python
# -*- coding: utf-8 -*-

import string


def rc(s):
    return s.translate(string.maketrans('ACGT', 'TGCA'))[::-1]


with open('rosalind_corr.txt') as f:
    ss = map(str.strip, f.readlines())
t = []
d = {}
for s in ss:
    d[s] = d.get(s, 0) + 1
    d[rc(s)] = d.get(rc(s), 0) + 1
good = [i for i in d if d[i] >= 2]
for s in ss:
    if d[s] == 1:
        for j in good:
            if sum(map(str.__ne__, s, j)) == 1:
                print s + '->' + j

