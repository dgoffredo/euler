#!/usr/bin/env python3

'''
Once again python makes this too easy.
'''

from sys import argv

default = 1000
powOf2 = default if len(argv) < 2 else int(argv[1])

print( sum(int(char) for char in str(2**powOf2)) )

