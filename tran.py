#!/usr/bin/python
# -*- coding: utf-8 -*-


def readdata(filename):
    with open(filename) as t:
        lines = t.readlines()
    currentId = None
    for s in lines + ['>']:
        if s[0] == '>':
            if currentId is not None:
                yield (currentId, ''.join(currentStrs))
            currentId = s.strip()[1:]
            currentStrs = []
        else:
            currentStrs.append(s.strip())


((name1, s1), (name2, s2)) = readdata('rosalind_tran.txt')
lat = ver = 0
for (c1, c2) in zip(s1, s2):
    if c1 == c2:
        pass
    elif set((c1, c2)) in (set('AG'), set('TC')):
        lat += 1
    else:
        ver += 1
print (lat + 0.0) / ver
