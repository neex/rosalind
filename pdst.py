#!/usr/bin/env python
from itertools import starmap
def readdata(filename):
    with open(filename) as t:
        lines = t.readlines()        
    currentId = None
    for s in lines + [">"]:
        if s[0] == ">":
            if currentId is not None:
                yield (currentId,"".join(currentStrs))
            currentId = s.strip()[1:]
            currentStrs = []
        else:
            currentStrs.append(s.strip())
data=list(readdata("rosalind_pdst.txt"))
for id1,data1 in data:
    for id2,data2 in data:
        print sum(starmap(str.__ne__,zip(data1,data2)))*1.0/len(data1),
    print
