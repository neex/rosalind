#!/usr/bin/python
# -*- coding: utf-8 -*-

with open('rosalind_dna.txt') as f:
    l = f.readline()
    print ' '.join(map(str, (l.count(x) for x in 'ACGT')))
