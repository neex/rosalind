#!/usr/bin/env python
from itertools import izip
with open("rosalind_cons.txt") as f:
    strs = filter(None, map(str.strip,f.readlines()))
d=dict((("A",[]),("C",[]),("G",[]),("T",[])))
acc=[]    
for s in izip(*strs):
    counts = [(s.count(c),c) for c in "ACGT"]
    for (count,char) in counts:
        d[char].append(count)
    acc.append(max(counts)[1])
print "".join(acc)
for c in "ACGT":
    print c+":"," ".join(map(str,d[c]))
