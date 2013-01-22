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


data = [(name, s[:3], s[-3:]) for (name, s) in readdata('rosalind_grph.txt')]
for (namef, preff, sufff) in data:
    for (namet, preft, sufft) in data:
        if namef != namet and sufff == preft:
            print namef, namet
