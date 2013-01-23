#!/usr/bin/python
# -*- coding: utf-8 -*-

with open('rosalind_sseq.txt') as f:
    (s, t) = map(str.strip, f.readlines())
    ps = 0
    for (num, c) in enumerate(s, 1):
        if c == t[ps]:
            print num,
            ps += 1
            if ps == len(t):
                print
                break

