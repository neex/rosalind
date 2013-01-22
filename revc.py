#!/usr/bin/env python
import string
with open("rosalind_revc.txt") as f:
    print f.readline().strip().translate(string.maketrans("ACGT","TGCA"))[::-1]
