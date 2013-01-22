#!/usr/bin/env python
with open("rosalind_sset.txt") as f:
    n=int(f.readline().strip())
    print reduce(lambda x,y:x*y%1000000,[2]*n,1)
