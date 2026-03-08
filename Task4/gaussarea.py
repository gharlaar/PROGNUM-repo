#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import scipy
import matplotlib.pyplot as plt
from scipy.integrate import quad

#Defining the function, constants and variables

def gauss(x, A, x0, sig, z0):
    return A*np.exp(-(x-x0)**2/(2*sig**2))+z0

A = float(input('Enter a value for A: '))
x0 = float(input('Enter a value for x0: '))
sig = float(input('Enter a value for sig: '))
z0 = float(input('Enter a value for z0: '))

x = np.linspace(-10, 10, 200)
y = gauss(x, A, x0, sig, z0)  #values for the given x


#Plotting the function

plt.plot(x, y, label = 'Function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Area under a Gaussian')
plt.grid(True)


# Finding the area using quad() and making the plot
x_low = float(input('Enter a value for the lower bound: '))
x_up = float(input('Enter a value for the upper bound: '))
area, error = scipy.integrate.quad(gauss, x_low, x_up, args = ( A, x0, sig, z0))
print(f"The area between x=0 and x=2.5 with its according error is {area}.")

plt.fill_between(x, y, where=(x >= x_low) & (x <= x_up), color = 'pink', alpha = 0.5, label = f'Calculated area = {area: .3f}')

plt.legend()
plt.show()






#make into executable script


# In[ ]:




