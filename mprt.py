#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import sys
with open('rosalind_mprt.txt') as f:
    ss = map(str.strip, f.readlines())
for id in ss:
    s = urllib2.urlopen('http://www.uniprot.org/uniprot/' + id + '.fasta').read().split('\n', 1)[1].replace('\n', '')
    ps = 0
    prev2 = ''
    prev1 = ''
    loc = []
    for (ind, c) in enumerate(s, 1):
        if ps == 0:
            if c == 'N':
                ps = 1
        elif ps == 1:
            if c != 'P':
                ps = 2
            else:
                ps = 0
        elif ps == 2:
            if c == 'S' or c == 'T':
                ps = 3
            elif prev1 == 'N' and c != 'P':
                ps = 2
            elif c == 'N':
                ps = 1
            else:
                ps = 0
        elif ps == 3:
            if c != 'P':
                loc.append(ind - 3)
                if prev2 == 'N' and (c == 'S' or c == 'T'):
                    ps = 3
                elif c == 'N':
                    ps = 1
                else:
                    ps = 0
            else:
                ps = 0
        prev2 = prev1
        prev1 = c
    if loc:
        print id
        print ' '.join(map(str, loc))
