#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 17:55:17 2020

@author: rshirale
"most of the time" is not all of the time, and when they don't it can lead to surprising consequences
"""
x = 0.0
for i in range(10):
    x = x + 0.1
if x == 1.0:
    print(x, '= 1.0')
else:
    print(x, 'is not 1.0')


