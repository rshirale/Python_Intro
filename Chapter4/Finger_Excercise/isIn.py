#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Finger exercise: Write a function isIn that accepts two strings as arguments and
returns True if either string occurs anywhere in the other, and False otherwise.
Hint: you might want to use the built-in str operation in.

"""
def isIn(sentenceOne, sentenceTwo):
    t = sentenceOne.split(' ')
    for c in t:
        if c in sentenceTwo:
            print('This word is common in both sentences:',c)
        else:
            print('Nothing is common between both strings')
    
sentenceOne = input('Enter a sentence: ')
sentenceTwo = input('Enter another sentence: ')

isIn(sentenceOne,sentenceTwo)
