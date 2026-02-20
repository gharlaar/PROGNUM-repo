#!/usr/bin/env python
# coding: utf-8

# In[2]:


from IPython.display import display, Math
from math import *

a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
c = float(input("Enter value for c: "))

D = b**2 - 4*a*c
if D < 0 or a == 0:
    print(f"This function has no solutions")
    
elif D > 0:
    x1 = (-b + sqrt(b**2 -4*a*c))/(2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    print(f"The solutions of the function are: {x1, x2}")

elif D==0:
    x1 = (-b + sqrt(b**2 -4*a*c))/(2*a)
    print(f"The solution of the function is: {x1}")



    


