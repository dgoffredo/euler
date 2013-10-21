#! /usr/bin/env python3

# This script solves problems 18 and 46

from array import array
from sys import argv, stdin
import re

def triNum(n):
    return n * (n+1) // 2

from math import sqrt

# Just a wrapper around an array that allows you to get/set
# values by (depth, x)
#
# depth
#  0     x:            0
#  1     x:          0   1
#  2     x:        0   1   2 
#  3     x:      0   1   2   3
#  .           .   .   .   .   .
#
class Triangle(object):
    def __init__(self, init):
        self.data = array('l', init)
        self._length = len(self.data)
        self._depth = int((sqrt(1 + 8 * (self._length - 1)) - 1) / 2) + 1 if self._length > 0 else 0

    def __getitem__(self, key):
        depth, x = key
        return self.getVal(depth, x)

    def __setitem__(self, key, value):
        depth, x = key
        return self.setVal(depth, x, value)

    def __iter__(self):
        for val in self.data:
            yield val

    def _keyToIndex(self, depth, x):
        assert depth < self._depth and x < depth + 1
        return triNum(depth) + x

    def getVal(self, depth, x):
        return self.data[self._keyToIndex(depth, x)]

    def setVal(self, depth, x, value):
        self.data[self._keyToIndex(depth, x)] = value

    @property
    def depth(self):
        return self._depth

inFile = open(argv[1]) if len(argv) > 1 else stdin

def readInts(inFile):
    for line in inFile:
        for word in re.sub(' +', ' ', line.strip()).split(' '):
            yield int(word)

tri = Triangle(readInts(inFile))

def parents(point):
    depth, x = point
    if depth < 1:
        return []
    return [ (depth - 1, px) for px in range(x-1, x+1) if px >=0 and px < depth ]

maxes = Triangle(tri) # a copy that will be overwritten with maximums

for depth in range(1, tri.depth):
    for x in range(depth + 1):
        maxes[(depth, x)] = tri[(depth, x)] + max(maxes[p] for p in parents((depth, x)))

print( max(maxes[(maxes.depth - 1, x)] for x in range(maxes.depth)) )

