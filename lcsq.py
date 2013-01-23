#!/usr/bin/python
# -*- coding: utf-8 -*-

with open('rosalind_lcsq.txt') as f:
    (a, b) = map(str.strip, f.readlines())
x = map(list, [[0] * (len(b) + 1)] * (len(a) + 1))
z = map(list, [[0] * (len(b) + 1)] * (len(a) + 1))
for i in xrange(1, len(a) + 1):
    for j in xrange(1, len(b) + 1):
        (x[i][j], z[i][j]) = max((x[i - 1][j], 1), (x[i][j - 1], 2), ((x[i - 1][j - 1] + 1 if a[i - 1] == b[j - 1] else -1), 3))
t = []
i = len(a)
j = len(b)
while i != 0 and j != 0:
    if z[i][j] == 3:
        t.append(a[i - 1])
        i -= 1
        j -= 1
    elif z[i][j] == 2:
        j -= 1
    else:
        i -= 1

print ''.join(t[::-1])

