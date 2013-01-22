#!/usr/bin/env python
with open("rosalind_iev.txt") as f:
    AAAA,AAAa,AAaa,AaAa,Aaaa,aaaa = map(int,f.readline().strip().split())
    print 2.0*(AAAA+AAAa+AAaa+AaAa*0.75+Aaaa*0.5)
    
