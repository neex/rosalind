#!/usr/bin/env python
with open("rosalind_lexv.txt") as f:
    alph=f.readline().strip().split()
    k=int(f.readline().strip())
stack=[""]*k
def rec(lev):
    if lev>0:
        print "".join(stack)
    if lev<k:
        for i in alph:
            stack[lev]=i
            rec(lev+1)
            stack[lev]=""
rec(0)    
