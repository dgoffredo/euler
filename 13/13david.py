#!/usr/bin/env python3

from sys import argv, stdin

inFile = open(argv[1]) if len(argv) > 1 else stdin
print(str(sum(int(line) for line in inFile))[:10])

