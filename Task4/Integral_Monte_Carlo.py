#!/usr/bin/env python
# coding: utf-8

# ***Question 4.6: Integral with Monte Carlo***

# In[1]:


import numpy as np
from math import *

#Giving the boundaries

Upper_boundary = float(input(f"Enter the upper boundary here: "))
Lower_boundary = float(input(f"Enter the lower boundary here: "))

#Defining the function

def f(Function, x):
    y = eval(Function)
    return y

Function = input(f"Enter an function here: ") #Giving the function
x = np.random.uniform(Lower_boundary, Upper_boundary, 1000) #Generating a list of values for x

total = sum(f(Function, x)) #Calculating the sum of the values for y

integralvalue = ((Upper_boundary - Lower_boundary)/1000) * total #Calculating the integral
print(f"So the value of the integral is {integralvalue}.")


# In[ ]:




