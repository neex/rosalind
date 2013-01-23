#!/usr/bin/python
# -*- coding: utf-8 -*-

with open('rosalind_edit.txt') as f:
    (a, b) = map(str.strip, f.readlines())
x = map(list, [[0] * (len(b) + 1)] * (len(a) + 1))
for i in xrange(0, len(a) + 1):
    for j in xrange(0, len(b) + 1):
        if i == 0 or j == 0:
            x[i][j] = max(i, j)
        else:
            x[i][j] = min(x[i - 1][j] + 1, x[i][j - 1] + 1, x[i - 1][j - 1] + ((0 if a[i - 1] == b[j - 1] else 1)))
print x[len(a)][len(b)]
