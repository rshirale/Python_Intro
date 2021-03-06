#!/usr/bin/env python3
"""
Bisection search approach to find square root of positive and negative numbers
"""
#Get users input
x = int(input("Enter an integer: "))

#close enough as answer that lies within some constant called epsilon
epsilon = 0.01

numGuesses = 0
#print(f"Value of numguesses before loop = {numGuesses}")

low = 0.0

high = max(1.0,abs(x))
#print(f"high: {high}")

# dividing search space in half at each step
ans = (high + low)/2.0

#block 1
while abs(ans**2 - abs(x)) >= epsilon:
    print(f"Low = {low}, High = {high}, Ans = {ans}")
    numGuesses += 1
    #print(f"Value of guesses in the loop = {numGuesses}")
    if  ans**2 < abs(x):
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0

if x < 0:
    ans = -ans
    print(f"number of guesses = {numGuesses}")
    print(f"{ans} is close to square root of {x}")
else:
    print(f"number of guesses = {numGuesses}")
    print(f"{ans} is close to square root of {x}")
