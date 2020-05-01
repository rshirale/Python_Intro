#!/usr/bin/env python3
"""
Approximation of the square root
"""
#Get users input
x = int(input("Enter an integer: "))

#close enough as answer that lies within some constant called epsilon
epsilon = 0.01

step = epsilon**2
#print(f"Value of step before loop = {step}")
numGuesses = 0
#print(f"Value of numguesses before loop = {numGuesses}")

ans = 0.0
#print(f"Value of ans before loop = {ans}")

#block 1
while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += step
    #print(f"Value of ans in the loop = {ans}")
    numGuesses += 1
    #print(f"Value of guesses in the loop = {numGuesses}")

print(f"number of guesses to find square root = {numGuesses}")
#block 2
if  abs(ans**2 - x) >= epsilon:
    print(f"Failed on square root of {x}")
else:
    print(f"{ans} is close to square root of {x}")
