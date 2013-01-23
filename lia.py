#!/usr/bin/python
# -*- coding: utf-8 -*-

import math


def logc(n, k):
    return -sum(map(math.log, xrange(1, k + 1))) - sum(map(math.log, xrange(1, n - k + 1))) + sum(map(math.log, xrange(1, n + 1)))


with open('rosalind_lia.txt') as f:
    (k, n) = map(int, f.readline().strip().split())
    logp = math.log(1.0 / 4)
    log1mp = math.log(1 - 1.0 / 4)
    ss = 0
    for i in xrange(n, 2 ** k + 1):
        ll = math.exp(logc(2 ** k, i) + logp * i + log1mp * (2 ** k - i))

#        print ll, math.exp(logc(2**k,i)) * ((1.0/8)**i) *(1-1.0/8)**(2**k-i)

        ss += ll
    print ss

