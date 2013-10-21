#!/usr/bin/env python3

'''
You have to go right n times and down n times, somehow. So you'll
have a string of 2*n symbols -- n rights and n downs.

You can arrange 2*n distinct symbols in (2*n)! ways, but
these are not distinct symbols. For each of of (2*n)! combinations
of 2*n symbols, you can rearrange the downs in any of n! ways, and
you can also rearrange the rights in any of n! ways, for a 
total "degeneracy" of (n!)**2. So, there are
    (2*n)! / (n!)**2
different ways to traverse an n x n grid using only down and right
moves.

Python makes this problem easy by handling big numbers natively.
If we were using machine integers, we'd have to be more clever about
calculating the factorials (we'd have to keep a running list of factors
for the numerator and denominator and eliminate as we go). Instead, I
just state the answer plainly.
'''

from math import factorial
from sys import argv

default = 20
n = default if len(argv) < 2 else int(argv[1])

# print( factorial(2*n) // factorial(n)**2 )
#
# Ok, I'll use a small optimization:
#
#     (2n)! / n!**2 = product(n + 1 to 2n) / n!
#
from operator import mul
from functools import reduce
print( reduce(mul, range(n+1, 2*n+1)) // factorial(n) ) 
