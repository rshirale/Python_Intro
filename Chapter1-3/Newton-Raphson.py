#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 16:48:44 2020
Newton-Raphson Method
@author: rshirale
"""
#Find x such that x**2-24 is within epsilon of 0

epsilon = 0.01
k= 24.0
numGuesses = 0 
guess = k/2.0
while abs(guess*guess - k) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2) -k)/(2*guess))
print('square root of', k, 'is about', guess)
print('Number of guesses it took to calculate square root is', numGuesses)


