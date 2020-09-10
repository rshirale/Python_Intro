# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 15:02:53 2020
polymorphic function example
@author: rshirale
"""
def readVal(valType, requestMsg, errorMsg):
    while True:
        val = input(requestMsg + '')
        try:
            return(valType(val)) #convert str to valType before returning
        except ValueError:
            print(val, errorMsg)

readVal(int, 'Enter an integer:', 'is not an integer')

