# -*- coding: utf-8 -*-
"""
Finger Excercise: Implement a function that meets the specifications below.
Use a try-except block.

"""
def sumDigits(s):
    """
    Assumes s is string 
    Returns the sum of decimal digits in s
        For example, if s is 'a2b3c' it returns 5
    """
    print(f"You entered this sentence \n")
    print(f"{s}")
    print()
    print(len(s))
 
t = str(input("Please enter the a string and find it's length: "))
sumDigits(t)
