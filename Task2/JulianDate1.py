#!/usr/bin/env python
# coding: utf-8

# In[13]:


Y1 = float(input(f"Enter year Y: "))
M1 = float(input(f"Enter month M: "))
D1 = float(input(f"Enter day D: "))

JD1 = 367*Y1 - 7*(Y1+(M1+9)//12)//4 - 3*((Y1+(M1-9)//7)//100 + 1)//4 + (275*M1)//9 + D1 + 1721029 - 0.5

print(JD1)

Y2 = float(input(f"Enter year Y: "))
M2 = float(input(f"Enter month M: "))
D2 = float(input(f"Enter day D: "))

JD2 = 367*Y2 - 7*(Y2+(M2+9)//12)//4 - 3*((Y2+(M2-9)//7)//100 + 1)//4 + (275*M2)//9 + D2 + 1721029 - 0.5

print(JD2)

difference = JD2-JD1

print(difference)

