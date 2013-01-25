#!/usr/bin/python
# -*- coding: utf-8 -*-

with open('rosalind_rnas.txt') as f:
    s = f.readline().strip()
x = map(list, [[0] * len(s)] * len(s))
allowededges = frozenset(map(frozenset, ('AU', 'CG', 'GU')))
for ln in xrange(1, len(s) + 1):

#    print "Calcalating len ",ln

    for start in xrange(0, len(s) - ln + 1):
        end = start + ln - 1
        if ln <= 4:
            x[start][end] = 1
        else:
            x[start][end] = x[start + 1][end]
            for conn in xrange(start + 4, end + 1):
                if frozenset((s[start], s[conn])) in allowededges:
                    temp = x[start + 1][conn - 1] * ((x[conn + 1][end] if conn != end else 1))
                    x[start][end] += temp
print x[0][len(s) - 1]
