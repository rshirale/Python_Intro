# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 10:05:59 2020
lambda expression
@author: rshirale
"""
L = []
for i in map(lambda x,y: x**y, [1,2,3,4],[3,2,1,0]):
    L.append(i)
print(L)

