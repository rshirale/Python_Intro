# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 16:31:15 2020

@author: rshirale
"""
#!/usr/bin/env python3
s = '1.23,2.4,3.123'
t = s.split(',')

total = 0
for c in t:
    print(c)
    total = total + float(c)

print(f"Total: {total}")