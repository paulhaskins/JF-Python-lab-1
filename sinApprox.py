# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 22:18:05 2022

@author: Paul Haskins

using monte carlo method of approximating the integral of sinx between 0 and 1
"""

import math
import random
import matplotlib.pyplot as plt
import numpy as np




def function(x):
    return math.sin(x_coord)

numbers = 0.0
in_area = 0.0
TotalArea = 1.0

AppA = []
xValues = []
yValues = []
x = np.linspace(0, 1, 100)

#true value of integral to many decimals
true_value = 0.4596976941318602825990633925570233962676895793820777723299027446



while numbers < 2000:
    x_coord = random.uniform(0, 1)
    y_coord = random.uniform(0, 1)
    
    xValues.append(x_coord)
    yValues.append(y_coord)
    
    
    #if below x^2 then the point is in the area
    if y_coord < function(x_coord):
        in_area +=1
        
    numbers +=1
    Approximation = in_area/numbers * TotalArea
   # print(Approximation)
    

    AppA.append([Approximation])
    
    

#Points under graph / total points = area under graph / total area
cumulative_inarea = np.cumsum(in_area)
cumulative_ratios=(cumulative_inarea/np.arange(1, numbers+1, dtype = np.float))



#Dots with top right quad

a = np.arange(0, 1, 0.1)
b = np.sin(a)


figsi = plt.figure()
figsi.set_size_inches(5, 5)
plt.plot(a, b)
plt.xlabel("x")
plt.ylabel("y")
plt.show()


#Dots with top right quad

a = np.arange(0, 1, 0.1)
b = np.sin(a)


figsi = plt.figure()
figsi.set_size_inches(5, 5)
plt.plot(a, b)
plt.plot(xValues, yValues, 'o', markersize= 0.5)
plt.xlabel("x")
plt.ylabel("y")
plt.show()



#graph Approx vs Exact value
plt.figure()
approx_area = plt.plot(AppA)
pi, = plt.plot(np.repeat(true_value, numbers))
# Restrict y-axis to [3.1, 3.3] so that more detail  is visible
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
