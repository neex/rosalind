#!/usr/bin/python
# -*- coding: utf-8 -*-

with open('rosalind_hamm.txt') as f:
    print sum(map(str.__ne__, f.readline(), f.readline()))
