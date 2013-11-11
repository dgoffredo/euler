#!/usr/bin/env python3

mathMax = 28123 # Theoretical lower bound on numbers
                # after which all can be written as
		# the sum of two abundant numbers.

mathMin = 12    # Smallest abundant number.

def isAbundant(i):
    return sum(f for f in range(1, i // 2 + 1) if i % f == 0) > i

abundants = [i for i in range(mathMin, mathMax - mathMin + 1) if isAbundant(i)]

sums = {a + b for a in abundants for b in abundants}

print(sum(s for s in range(mathMax + 1) if s not in sums)) # answer
