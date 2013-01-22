#!/usr/bin/env python
from itertools import starmap
with open("rosalind_hamm.txt") as f:
    print sum(starmap(str.__ne__,zip(f.readline(),f.readline())))
