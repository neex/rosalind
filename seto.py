#!/usr/bin/python
# -*- coding: utf-8 -*-


def ps(s):
    return '{' + ', '.join(map(str, sorted(list(s)))) + '}'


with open('rosalind_seto.txt') as f:
    n = int(f.readline().strip())
    set1 = set(map(int, f.readline().translate(None, ' {}').split(',')))
    set2 = set(map(int, f.readline().translate(None, ' {}').split(',')))
    setF = set(range(1, n + 1))
    print ps(set1.union(set2))
    print ps(set1.intersection(set2))
    print ps(set1 - set2)
    print ps(set2 - set1)
    print ps(setF - set1)
    print ps(setF - set2)

