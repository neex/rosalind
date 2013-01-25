#!/usr/bin/python
# -*- coding: utf-8 -*-

with open('rosalind_scsp.txt') as f:
    (a, b) = map(str.strip, f.readlines())
x = map(list, [[0] * (len(b) + 1)] * (len(a) + 1))
z = map(list, [[0] * (len(b) + 1)] * (len(a) + 1))
for i in xrange(0, len(a) + 1):
    for j in xrange(0, len(b) + 1):
        if i == 0:
            (x[i][j], z[i][j]) = (j, 2)
        elif j == 0:
            (x[i][j], z[i][j]) = (i, 1)
        else:
            (x[i][j], z[i][j]) = min((x[i - 1][j] + 1, 1), (x[i][j - 1] + 1, 2), ((x[i - 1][j - 1] + 1 if a[i - 1] == b[j - 1] else 10000000), 3))
t = []
i = len(a)
j = len(b)
while i != 0 or j != 0:
    if z[i][j] == 3:
        t.append(a[i - 1])
        i -= 1
        j -= 1
    elif z[i][j] == 2:
        t.append(b[j - 1])
        j -= 1
    else:
        t.append(a[i - 1])
        i -= 1

print ''.join(t[::-1])
