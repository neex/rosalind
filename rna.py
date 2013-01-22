#!/usr/bin/python
# -*- coding: utf-8 -*-

with open('rosalind_rna.txt') as f:
    print f.readline().strip().replace('T', 'U')
