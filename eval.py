#!/usr/bin/python
# -*- coding: utf-8 -*-

with open('rosalind_eval.txt') as f:
    n = int(f.readline().strip())
    s = f.readline().strip()
    for l in map(float, f.readline().strip().split()):
        p = reduce(float.__mul__, ((l / 2 if x in 'GC' else (1 - l) / 2) for x in s), 1.0)
        print p * (n - len(s) + 1),
    print

