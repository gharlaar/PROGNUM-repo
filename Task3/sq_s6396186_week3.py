#!/usr/bin/env python
# coding: utf-8

# * Name: Githa Harlaar
# * Username:  gharlaar
# * Student number: S6396186
# * Group (AS1, etc.): AS5
# 
# 

# **Question 3.1: Average Calculator**

# In[21]:


masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e22] #in kg?

print(f"These masses in the list are bigger than the moon's mass:")
for M in masses:
    if M > 7.349e+22: #bigger than the moon's mass
        print(M)

print()
nmasses = masses[6:] #new masses
print(f"The list with only the last 5 masses is {list(nmasses)}")

print()

print(f"The total mass is {sum(nmasses)} kg") #total of the components in kg
print(f"The total number of components is {len(nmasses)}")
print(f"So, the average mass of the last five masses is {sum(nmasses)/len(nmasses)} kg")

