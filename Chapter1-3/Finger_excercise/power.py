#!/usr/bin/env python3
"""
Write a program that asks the user to enter an integer.
Prints two integers, root and pwr,
such that 1<pwr<6
and root**pwr

"""
while True:
    pwr = int(input("Enter an integer: "))
    if pwr >= 1 and pwr <= 6:
        break
print(f"Power is {pwr}")
print(f"root is root**{pwr}")
