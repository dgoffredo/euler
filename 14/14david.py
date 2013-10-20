#!/usr/bin/env python3

def collatz(n):
    if n % 2: # n odd
        return  3 * n + 1
    else:     # n even
        return n // 2

# starting values from the initial cycle
# 4 --> 2 --> 1
startOfLongest = 4   # Where we start.
longestSequence = {4, 2, 1} # Set of hops.

for start in range(3, 1000000):
    val = start
    values = {val}
    
    while val not in longestSequence:
        val = collatz(val)
        values.add(val)

    if val == startOfLongest: # we hit the top
        # Now we have a new max
        startOfLongest = start
        longestSequence |= values
        print('New max of {} hops found starting from {}'.format(len(longestSequence), startOfLongest))

print(startOfLongest) # the answer

