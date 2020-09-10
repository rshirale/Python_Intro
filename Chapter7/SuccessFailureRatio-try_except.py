# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 14:15:39 2020
SuccessFailureRatio try-except block
@author: rshirale
"""
numSuccesses = 2
numFailures = 0

try:
    SuccessFailureRatio = numSuccesses/numFailures
    print('The success/failure ratio is', SuccessFailureRatio)
except ZeroDivisionError:
    print('No failures, do the success/failure ratio is undefined')
print('Now here')




