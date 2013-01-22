#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

with open('rosalind_prob.txt') as f:
    s = f.readline().strip()
    gcs = map(float, f.readline().strip().split())

for x in gcs:
    d = {}
    d['C'] = d['G'] = math.log(x / 2) / math.log(10)
    d['T'] = d['A'] = math.log((1 - x) / 2) / math.log(10)
    print sum(map(d.get, s)),
print
