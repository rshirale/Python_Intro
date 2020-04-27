#!/usr/bin/env python3
"""
Find the cube root of a perfect cube using Exhaustive Enumeration Technique
Prints the integer cube rootm if it exists, of an integer
"""
x = int(input("Enter an integer: "))

for ans in range(0, abs(x)+1):
    if ans**3 >= abs(x):
        break
if ans**3 != abs(x):
    print(f"{x}, is not a perfect cube")
else:
    if x < 0:
        ans = -ans
    print(f"Cube root of {x} is {ans}")
