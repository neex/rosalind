#!/usr/bin/env python
with open("rosalind_iprb.txt") as f:
    dom,hete,rec=map(int,f.readline().strip().split())
    n=dom+hete+rec
    print 1.0*(dom*(hete+rec)+dom*(dom-1)/2+hete*rec*0.5+hete*(hete-1)/2*0.75)/(n*(n-1)/2)
