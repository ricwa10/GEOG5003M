# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 15:53:40 2022

@author: richa
"""

import random

# Set up first pair of coordinates within a 100x100 grid.
y0 = random.randint(0,99)
x0 = random.randint(0,99)

# Random walk one step (first pair).
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1
    
if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1

print("y0 = " + str(y0), "and", "x0 = " + str(x0))

# Set up second pair of coordinates within a 100x100 grid.
y1 = random.randint(0,99)
x1 = random.randint(0,99)

# Random walk one step (second pair).
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1
    
if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1

print("y0 = " + str(y1), "and", "x0 = " + str(x1))

# Calculating the distance between both pair of variables after moving
distance = ((y0 - y1)**2 + (x0 - x1)**2)**0.5

print("Distance between (y0,x0) and (y1,x1) =", round(distance,2))