# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 22:52:30 2020
Sequences and Multiple Assignment
@author: rshirale
"""
def findExtremeDivisor(n1, n2):
    """Assumes that n1 and n2 are positive ints
    Returns a tuple containing the smallest common divisor > 1 and
    the largest common divisor of n1 and n2. If no common divisor,
    other than 1, returns (None, None)"""
    
    print('n1 is ',n1)
    print('n2 is ',n2)
    minVal, maxVal = None, None
    for i in range(2, min(n1,n2) + 1):
        if n1%i == 0 and n2%i == 0:
            if minVal == None:
                minVal = i
            maxVal = i
    return(minVal, maxVal)

minDivisor, maxDivisor = findExtremeDivisor(100,200)

print('minDivisor =',minDivisor, 'maxDivisor =', maxDivisor)


