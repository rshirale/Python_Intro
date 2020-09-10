# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 22:46:38 2020
A for statement used to iterate over the elements of a tuple
@author: rshirale
"""
def intersect(t1,t2):
    """Assumes t1 and t2 are tuples
    Returns a tuple contaning elements that are in 
    both t1 and t2"""
    result = ()
    for e in t1:
        if e in t2:
            result += (e,)
    print(result)
    return result
    


t1 = (1, 'two', 3)
t2 = (1, 3.25, 'two')

intersect(t1,t2)