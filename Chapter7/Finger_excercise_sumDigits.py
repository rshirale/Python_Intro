# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 14:22:18 2020
Finger exercise try-except
@author: rshirale
"""
def sumDigits(s):
    """Assumes s is a string
       Returns the sum of the decimal digit in s
        For example, if s is 'a2b3c' it returns 5 """
    counter = 0
    result = []
    for elem in s:
        try:
            value = int(elem)
            counter = counter + value
        except ValueError:
            result.append(elem)
            
    print('Sum of decimal digits in s is:',counter)    
    print('These strings were foung in input data', result)

data = 'a2b3c'
sumDigits(data)


