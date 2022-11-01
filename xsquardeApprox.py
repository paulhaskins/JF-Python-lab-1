# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 21:44:56 2022

@author: Paul Haskins
"""

import math
import random
import matplotlib.pyplot as plt
import numpy as np


def function(x):
    return x ** 2

numbers = 0.0
in_area = 0.0
TotalArea = 1.0

AppA = []
xValues = []
yValues = []
x = np.linspace(0, 1, 100)
true_value = 1/3

while numbers < 20000:
    x_coord = random.uniform(0, 1)
    y_coord = random.uniform(0, 1)
    
    xValues.append(x_coord)
    yValues.append(y_coord)

    #if below x^2 then the point is in the area
    if y_coord < function(x_coord):
        in_area +=1
        
    numbers +=1
    Approximation = in_area/numbers * TotalArea
    AppA.append([Approximation])


    

#Points under graph / total points = area under graph / total area
print(in_area/numbers * TotalArea) 


#graph dem dots
fig = plt.figure()
fig.set_size_inches(5, 5)
plt.plot(x, x ** 2)
plt.xlabel("x")
plt.xlabel("y")
plt.show()

#graph dem dots
fig = plt.figure()
fig.set_size_inches(5, 5)
plt.plot(x, x ** 2)
plt.plot(xValues, yValues, 'o', markersize= 0.5)
plt.xlabel("x")
plt.xlabel("y")
plt.show()


cumulative_inarea = np.cumsum(in_area)
cumulative_ratios =(cumulative_inarea/np.arange(1, numbers+1, dtype = np.float))

#graph Approx vs Exact value
plt.figure()
approx_area = plt.plot(AppA)
pi, = plt.plot(np.repeat(true_value, numbers))
plt.ylim(0, 1)
plt.xlabel("Sample size")
plt.legend([approx_area,pi],["Approximation", "Exact value"])



def cummean(arr):
    return np.cumsum(arr)/np.arange(1,len(arr)+1,dtype=np.float)

def cumstd(arr):
    return np.sqrt(cummean(arr ** 2) - cummean(arr) ** 2)

#Standard deviation vs Sample size
plt.figure()
stdevs, = plt.plot(cumstd(cumulative_ratios))
plt.legend([stdevs], ["Standard deviation"])
plt.xlabel("Sample size")


