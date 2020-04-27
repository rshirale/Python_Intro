#!/usr/bin/env python3
"""
Find the cube root of a perfect cube using Exhaustive Enumeration Technique
Prints the integer cube rootm if it exists, of an integer
"""
x = int(input("Enter an integer: "))
ans = 0
while ans**3 < abs(x):
    ans += 1

print(f"\nWhile loop iterations ans:{ans}")
if ans**3 != abs(x):
    print(f"\n{x}, is not a perfect cube")
else:
    if x < 0:
        ans = -ans
    print(f"\nCube root of {x} is {ans}")
