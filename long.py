#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
with open('rosalind_long.txt') as f:
    strs = filter(None, map(str.strip, f.readlines()))
mm = []
n = len(strs)
for i in strs:
    tt = []
    mm.append(tt)
    for j in strs:
        if i != j:
            needle = j + '#' + i
            prefix_function = [0]
            last = 0
            for c in needle[1:]:
                while last > 0 and needle[last] != c:
                    last = prefix_function[last - 1]
                if needle[last] == c:
                    last += 1
                prefix_function.append(last)
            if last >= len(i) / 2 + 1 and last >= len(j) / 2 + 1:
                tt.append(last)
            else:
                tt.append(0)
        else:
            tt.append(0)

stack = []
used = [0] * n


def rec(v):
    if used[v]:
        return False
    used[v] = 1
    stack.append(v)
    if len(stack) == n:
        return True
    for (i, s) in enumerate(mm[v]):
        if s:
            if rec(i):
                return True
    stack.pop()
    used[v] = 0
    return False


for i in xrange(n):
    if rec(i):
        prev = None
        tt = []
        for j in stack:
            if prev == None:
                tt.append(strs[j])
            else:
                tt.append((strs[j])[mm[prev][j]:])
            prev = j
        print ''.join(tt)
