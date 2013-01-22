#!/usr/bin/env python
with open("rosalind_pper.txt") as f:
    n,k=map(int,f.readline().strip().split())
    print reduce(lambda x,y:x*y%1000000,range(n,n-k,-1),1)
