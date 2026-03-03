#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
user = input("Enter R (rock), P (paper) or S (scissors): ")

programme = np.array(["R", "P", "S"])  #Where the computer can choose from
randindx = np.random.randint(0, len(programme), 1) #Gives either R, P or S
bot = programme[randindx] #Couples the programme to the randindx
print(f"The bot gives... {bot}!")

#Conditions and rules of the game

if user == "R" and bot == "S":
    print(f"User wins!")
elif user == bot:
    print(f"It's a tie!")
elif user == "P" and bot == "R":
    print(f"User wins!")
elif user == "S" and bot == "P":
    print(f"User wins!")
elif bot == "R" and user == "S":
    print(f"Bot wins!")
elif bot == "P" and user == "R":
    print(f"Bot wins!")
elif bot == "S" and user == "P":
    print(f"Bot wins!")


# In[ ]:




