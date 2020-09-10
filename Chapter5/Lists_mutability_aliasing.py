# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 07:56:59 2020
Lists, mutability and aliasing
@author: rshirale
"""
Techs = ['MIT','Caltech']
Ivys = ['Harvard','Yale','Brown']

Univs = [Techs,Ivys]
UnivsNew = [['MIT','Caltech'],['Harvard','Yale','Brown']]

print('Univs =', Univs)
print('UnivsNew =', UnivsNew)
print(Univs==UnivsNew) # test value equality
print(id(Univs)==id(UnivsNew)) # test object equality
print('Id of Univs = ',id(Univs))
print('Id of UnivsNew = ',id(UnivsNew))
