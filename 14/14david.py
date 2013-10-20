#!/usr/bin/env python3

def collatz(n, count): # Increments count for convenience
    if n % 2: # n odd
        return  (3 * n + 1, count + 1)
    else:     # n even
        return (n // 2, count + 1)

# starting values from the initial cycle
# 1 --> 2 --> 4 --> 2 --> 1
startOfLongest = 2  # Where we start.
lengthOfLongest = 3 # Length in hops.

for start in range(3, 1000000):
    count = 0
    val = start
    val, count = collatz(val, count)
    
    while val != startOfLongest:
        val, count = collatz(val, count)
        break
    if val == startOfLongest: # if we didn't break explicitly
        # Now we have a new max
        startOfLongest = start
        lengthOfLongest += count

print(startOfLongest) # the answer
# print(lengthOfLongest)
