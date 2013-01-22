#!/usr/bin/env python
import collections
class Node:
    mark_overall = 0
    def __init__(self):
        self.s = {}
        Node.mark_overall +=1
        self.mark = Node.mark_overall
    def __repr__(self):
        return "Node (mark=%s, d=%s)" % (self.mark,self.s)
with open("rosalind_trie.txt") as f:
    strs = filter(None, map(str.strip,f.readlines()))
root = Node()
for mark,s in enumerate(strs,1):
    cur = root
    for c in s:
        if not c in cur.s:
            cur.s[c] = Node()
        cur = cur.s[c]
def outtrie(t):
    for x in t.s:
        print t.mark,t.s[x].mark,x
        outtrie(t.s[x])
outtrie(root)
