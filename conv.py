#!/usr/bin/python
# -*- coding: utf-8 -*-

with open('rosalind_conv.txt') as f:
    (a, b) = (map(float, f.readline().strip().split()) for ll in (0, 1))
    ll = sorted(i - j for i in a for j in b)
    mxc = 0
    mxr = 0
    t = 0
    prev = -100000000000.0
    for i in ll:
        if i - prev > 0.0000001:
            t = 0
        t += 1
        prev = i
        if mxc < t:
            mxc = t
            mxr = i

    print mxc
    print mxr
