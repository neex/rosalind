#!/usr/bin/python
# -*- coding: utf-8 -*-


def gen_subs(haystack, needle):
    prefix_function = [0]
    last = 0
    for c in needle[1:]:
        while last > 0 and needle[last] != c:
            last = prefix_function[last - 1]
        if needle[last] == c:
            last += 1
        prefix_function.append(last)
    pos = 0
    for (hpos, c) in enumerate(haystack):
        while pos > 0 and c != needle[pos]:
            pos = prefix_function[pos]
        if c == needle[pos]:
            pos += 1
        if pos == len(needle):
            yield hpos - len(needle) + 1
            pos = prefix_function[pos - 1]


with open('rosalind_subs.txt') as f:
    print ' '.join(map(str, map(int(1).__add__, gen_subs(f.readline().strip(), f.readline().strip()))))

