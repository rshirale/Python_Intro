#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Finger exercise: Write a function isIn that accepts two strings as arguments and
returns True if either string occurs anywhere in the other, and False otherwise.
Hint: you might want to use the built-in str operation in.

"""
# Initiating function to compare both sentences
def isIn(sentenceOne, sentenceTwo):
    
    #converting sentences from upper case to lower case, this to have all alphabets in same format
    sentenceOne = sentenceOne.lower()
    sentenceTwo = sentenceTwo.lower()
    
    # This statement evaluates is there is space in sentences, if space exists Part 1 runs, else Part 2 runs
    if " " in sentenceOne and sentenceTwo:
        #Part 1
        print('*****************************************************************')
        print('Sentence One is:',sentenceOne)
        print('Sentence Two is:',sentenceTwo)
        print()
        
        present = 0
        not_present = 0
        spliter = sentenceOne.split(' ')
        
        for c in spliter:
            if c in sentenceTwo:
                print('Output: Word "{}" is present in both sentences'.format(c))
                present = present + 1
            else:
                print('Output: Word "{}" is NOT present in both sentences'.format(c))
                not_present =+ 1
        print()
        print('Results: {} word/s present in both sentences'.format(present))
        print('Results: {} word/s not present in both sentences'.format(not_present))
        print('*****************************************************************')
        print()
    else:
        #Part 2
        print('*****************************************************************')
        print('String One is:',sentenceOne)
        print('String Two is:',sentenceTwo)
        print()
        present = 0
        not_present = 0
        for c in sentenceOne:
            if c in sentenceTwo:
                present = present + 1
            else:
                not_present =+ 1
        print('Results: {} string/s is present in both sentences'.format(present))
        print('Results: {} string/s not is present in both sentences'.format(not_present))
        print('*****************************************************************')
        print()            

# Test function to try various combinations for strings and sentences!
def testisIn():
    print(f"Scenario 1: Testing sentences if either word appear in ther other")
    sentenceOne = 'Tim and Jill are friends'
    sentenceTwo = 'tim jill are not friends'
    isIn(sentenceOne,sentenceTwo)

    print(f"Scenario 2: Testing sentences if either word DO NOT appear in ther other")
    sentenceOne = 'Tim and Jill are friends'
    sentenceTwo = 'Tom Hill were rivals'
    isIn(sentenceOne,sentenceTwo)
    
    print(f"Scenario 3: Testing for random strings if either string appear in ther other")
    sentenceOne = 'hfhsdfksdhfio'
    sentenceTwo = 'eqwpojfnlas'
    isIn(sentenceOne,sentenceTwo)
    
testisIn()