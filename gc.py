#!/usr/bin/env python
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
            
(perc,name) = max([(100.0 * len(val.translate(None, "AT")) / len(val),name) for name,val in readdata("rosalind_gc.txt")])
print name
print str(perc)+"%"

