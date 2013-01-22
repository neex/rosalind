#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools
with open('rosalind_perm.txt') as f:
    n = int(f.readline().strip())

perms = list(itertools.permutations(range(1, n + 1)))
print len(perms)
for i in perms:
    print ' '.join(map(str, i))

