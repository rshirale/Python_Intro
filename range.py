#!/usr/bin/env python3
x = 4
for j in range(x):
    print(f"J: Outer loop {j}")
    for i in range(x):
        print(f"I: Inner loop {i}")
        x=2
