#!/usr/bin/env python3
"""
Find the cube root of a perfect cube using Exhaustive Enumeration Technique
Prints the integer cube rootm if it exists, of an integer
"""
x = int(input("Enter an integer: "))
print(f"You have enetered x as {x}")
for ans in range(0, abs(x)+1):
    print(f"Value before if statement of ans: {ans} and x: {x}")
    if ans**3 >= abs(x):
        print(f"if statment with ans value {ans} and x value {x}")
        break
print(f"ans after break is {ans} and x is {x}")
if ans**3 != abs(x):
    print(f"{x}, is not a perfect cube")
else:
    if x < 0:
        print(f"Value of ans right after the start of if x < 0 and:{ans}")
        ans = -ans
    print(f"Cube root of {x} is {ans}")
