#!/usr/bin/python
# -*- coding: utf-8 -*-

with open('rosalind_tree.txt') as f:
    n = int(f.readline().strip())
    print n - 1 - len(filter(None, map(str.strip, f.readlines())))

