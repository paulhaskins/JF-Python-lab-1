# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 15:42:31 2022

@author: prcha
"""

import matplotlib.pyplot as plt
import numpy as np



circle_x = np.linspace(0, 1, 100)
circle_y = np.sqrt(1-circle_x**2)

fig1 = plt.figure()
fig1.set_size_inches(5, 5)
plt.plot(circle_x, circle_y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

times = 2000
x = np.random.rand(times)
y = np.random.rand(times)

#Dots with top right quad
fig2 = plt.figure()
fig2.set_size_inches(5, 5)
plt.plot(x, y, 'o', markersize=1)
plt.plot(circle_x, circle_y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

#inside or outside circle
dist = np.sqrt(x ** 2 + y ** 2)
incircle = dist <= 1
outcircle = dist > 1

incircle_ratio=float(np.sum(incircle))/float(len(incircle))

pi = incircle_ratio * 4
print(pi)

cumulative_incircle = np.cumsum(incircle)

cumulative_ratios=(cumulative_incircle/np.arange(1,times+1,dtype=np.float))

pis = cumulative_ratios * 4

#Approx vs Exact value
plt.figure()
approx_pis, = plt.plot(pis)
pi, = plt.plot(np.repeat(np.pi, times))
# Restrict y-axis to [3.1, 3.3] so that more detail  is visible
plt.ylim(3.1, 3.3)
plt.xlabel("Sample size")
plt.legend([approx_pis,pi],["Approximation", "Exact value"])

def cummean(arr):
    return np.cumsum(arr)/np.arange(1,len(arr)+1,dtype=np.float)


def cumstd(arr):
    return np.sqrt(cummean(arr ** 2) - cummean(arr) ** 2)

#Standard deviation vs Sample size
plt.figure()
stdevs, = plt.plot(cumstd(pis))
plt.legend([stdevs], ["Standard deviation"])
plt.xlabel("Sample size")








