#!/usr/bin/python
# -*- coding: utf-8 -*-

import math


def logc(n, k):
    return -sum(map(math.log, xrange(1, k + 1))) - sum(map(math.log, xrange(1, n - k + 1))) + sum(map(math.log, xrange(1, n + 1)))


with open('rosalind_indc.txt') as f:
    n = int(f.readline().strip())
    ss = []
    for i in xrange(0, 2 * n + 1):
        ss.append(math.exp(logc(2 * n, i) + math.log(0.5) * 2 * n))
    print ' '.join(map(str, map(math.log(10).__rdiv__, map(math.log, (sum(ss[i:]) for i in xrange(1, 2 * n + 1))))))

