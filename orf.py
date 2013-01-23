#!/usr/bin/python
# -*- coding: utf-8 -*-

import string

dictionary = dict((
    ('UUU', 'F'),
    ('CUU', 'L'),
    ('AUU', 'I'),
    ('GUU', 'V'),
    ('UUC', 'F'),
    ('CUC', 'L'),
    ('AUC', 'I'),
    ('GUC', 'V'),
    ('UUA', 'L'),
    ('CUA', 'L'),
    ('AUA', 'I'),
    ('GUA', 'V'),
    ('UUG', 'L'),
    ('CUG', 'L'),
    ('AUG', 'M'),
    ('GUG', 'V'),
    ('UCU', 'S'),
    ('CCU', 'P'),
    ('ACU', 'T'),
    ('GCU', 'A'),
    ('UCC', 'S'),
    ('CCC', 'P'),
    ('ACC', 'T'),
    ('GCC', 'A'),
    ('UCA', 'S'),
    ('CCA', 'P'),
    ('ACA', 'T'),
    ('GCA', 'A'),
    ('UCG', 'S'),
    ('CCG', 'P'),
    ('ACG', 'T'),
    ('GCG', 'A'),
    ('UAU', 'Y'),
    ('CAU', 'H'),
    ('AAU', 'N'),
    ('GAU', 'D'),
    ('UAC', 'Y'),
    ('CAC', 'H'),
    ('AAC', 'N'),
    ('GAC', 'D'),
    ('UAA', ''),
    ('CAA', 'Q'),
    ('AAA', 'K'),
    ('GAA', 'E'),
    ('UAG', ''),
    ('CAG', 'Q'),
    ('AAG', 'K'),
    ('GAG', 'E'),
    ('UGU', 'C'),
    ('CGU', 'R'),
    ('AGU', 'S'),
    ('GGU', 'G'),
    ('UGC', 'C'),
    ('CGC', 'R'),
    ('AGC', 'S'),
    ('GGC', 'G'),
    ('UGA', ''),
    ('CGA', 'R'),
    ('AGA', 'R'),
    ('GGA', 'G'),
    ('UGG', 'W'),
    ('CGG', 'R'),
    ('AGG', 'R'),
    ('GGG', 'G'),
    ))

with open('rosalind_orf.txt') as f:
    s = f.readline().strip()

srev = s.translate(string.maketrans('ACGT', 'TGCA'))[::-1]

s = s.replace('T', 'U')
srev = srev.replace('T', 'U')
printed = set()

for ss in (tt[i:] for tt in (s, srev) for i in xrange(len(tt))):
    if ss[:3] == 'AUG':
        i = 0
        t = []
        while True:
            if i >= len(ss):
                break
            if not ss[i:i + 3] in dictionary:
                break
            cc = dictionary[ss[i:i + 3]]
            if cc == '':
                cand = ''.join(t)
                if not cand in printed:
                    print cand
                    printed.add(cand)
                break
            else:
                t.append(cc)
                i += 3
