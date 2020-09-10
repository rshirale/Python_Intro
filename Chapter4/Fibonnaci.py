#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 21:35:47 2020
Recursive implementation of Fibonnaci sequence
@author: rshirale
"""
def fib(n):
    """Assumes n int >= 0
        Returns Fibonnaci of n"""
    if n==0 or n==1:
        return 1
    else:
        if fib(n-1) == 2 or fib(n-2) == 2:
            print('f(',fib(n-1),') and f(',fib(n-2),')')
        return fib(n-1) + fib(n-2)

def testFib(n):
    for i in range(n+1):
        print('fib of', i, '=', fib(i))
        
testFib(5)

