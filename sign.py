#!/usr/bin/python
# -*- coding: utf-8 -*-

with open('rosalind_sign.txt') as f:
    n = int(f.readline().strip())
    print reduce(int.__mul__, range(1, n + 1), 1) * 2 ** n
    for t in itertools.permutations(range(1, n + 1)):
        for i in xrange(2 ** n):
            print ' '.join(map(str, map(int.__mul__, t, map(int(-1).__pow__, map(int, bin(i)[2:].zfill(n))))))

