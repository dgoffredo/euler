#!/usr/bin/env python3

from random import randint
from sys import stdout, argv

if len(argv) == 0:
    print('I will output to a file an N x N grid of random integers in [0, MAX-1]')

N = int(input('N = ')) if len(argv) < 2 else int(argv[1])
MAX = int(input('MAX = ')) if len(argv) < 3 else int(argv[2])
out = stdout if len(argv) < 4 else argc[3] # output file
 
for _ in range(N):
    out.write(' '.join(str(randint(0, MAX-1)) for _ in range(N)) + '\n')
