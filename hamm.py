#!/usr/bin/env python
with open("rosalind_hamm.txt") as f:
    print sum(map(lambda t: str.__ne__(*t),zip(f.readline(),f.readline())))
