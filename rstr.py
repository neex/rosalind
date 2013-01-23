#!/usr/bin/python
# -*- coding: utf-8 -*-

with open('rosalind_rstr.txt') as f:
    (n, p) = map(float, f.readline().strip().split())
    s = f.readline().strip()
    pp = 1
    for c in s:
        pp = pp * ((p / 2 if c in 'GC' else (1 - p) / 2))
    pp = 1 - (1 - pp) ** n
    print pp

