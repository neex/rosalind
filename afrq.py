#!/usr/bin/python
# -*- coding: utf-8 -*-

with open('rosalind_afrq.txt') as f:
    gcs = map(float, f.readline().strip().split())
for a in gcs:
    x = -a + 2 * a ** 0.5
    print x,
print
