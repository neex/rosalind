#!/usr/bin/python
# -*- coding: utf-8 -*-

with open('rosalind_kmp.txt') as f:
    s = f.readline().strip()
    prefix_function = [0]
    last = 0
    for c in s[1:]:
        while last > 0 and s[last] != c:
            last = prefix_function[last - 1]
        if s[last] == c:
            last += 1
        prefix_function.append(last)
    print ' '.join(map(str, prefix_function))

