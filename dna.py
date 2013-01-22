#!/usr/bin/env python
with open("rosalind_dna.txt") as f:
    l = f.readline()
    print " ".join(map(str,(l.count(x) for x in "ACGT")))
