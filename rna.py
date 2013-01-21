#!/usr/bin/env python
with open("rosalind_rna.txt") as f:
    print f.readline().strip().replace('T','U')
