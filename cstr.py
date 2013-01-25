#!/usr/bin/python
# -*- coding: utf-8 -*-

with open('rosalind_cstr.txt') as f:
    for k in set([''.join(map(str, map(int, map(s[0].__eq__, s)))) for s in map(''.join, zip(*filter(None, map(str.strip, f.readlines()))))]):
        if sum(map(int, k)) not in (0, 1, len(k), len(k) - 1):
            print k
