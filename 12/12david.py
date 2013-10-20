#!/usr/bin/env python3

def isOdd(n):
    return n % 2 != 0

def factorsOf(n):
    return [f for f in range(1, n+1) if n % f == 0]

# n'th triangle number is t(n) := n(n+1)/2
# and the number factors of t(n) are a function
# of the factors in n/2 and n+1 (if n is even)
# or (n+1)/2 and n (if n is odd).

# The trick is to notice that t(n) and t(n+1)
# share a factor: namely, (n+1). So you need
# calculate the factors of (n+1) only once for
# two adjacent numbers. This makes the problem
# scale much more nicely. I use the list 'sharedFactors'
# here to store those unchanged values between any two iterations.


def triNum(n):
    return n * (n+1) // 2

def naturalNumbers(skip=1):
    n = 1
    yield n
    while True: # forever
        n += skip
        yield n
        
from itertools import product # cartesian product
def combinedNumFactors(seq1, seq2):
    return len({a * b for a, b in product(seq1, seq2)})

def announceNewMax(newMax, triangNum):
    print('Found new maximum number of factors {} for {}.'.format(newMax, triangNum))
    if newMax > 500:
        print(triangNum) # final result
        quit()
    return newMax

# Here's the meat of the algorithm
def updateMax(sharedFactors, maxSoFar, n):
    newPart = (n+1) // 2 if isOdd(n) else n+1
    oldFactors = sharedFactors
    newFactors = factorsOf(newPart)
    numFactors = combinedNumFactors(oldFactors, newFactors)
    if numFactors > maxSoFar:
        maxSoFar = announceNewMax(numFactors, triNum(n))
    return (newFactors, maxSoFar)

maxSoFar = 0
sharedFactors = [1]

for n in naturalNumbers():
    sharedFactors, maxSoFar = updateMax(sharedFactors, maxSoFar, n)

