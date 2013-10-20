#!/usr/bin/env python3

def numFactors(num):
    count = 0
    for i in range(1,num+1):
         if num % i == 0:
             count += 1
    return count;

def triangNum(num):
    return num * (num + 1) // 2

def naturalNumbers():
    n = 0
    while True: # forever
        n +=1
        yield n
        
maxNumFound = 0
for n in naturalNumbers():
    numFactorsFound = numFactors(triangNum(n))
    if numFactorsFound > maxNumFound:
        maxNumFound = numFactorsFound
        print('Found new max of {} factors for number {}'.format(maxNumFound, triangNum(n)))
    if numFactors(triangNum(n)) > 500:
        print(triangNum(n))
        break
