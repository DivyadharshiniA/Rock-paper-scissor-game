#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random
ui=int(input("Enter a number 0 for rock, 1 for paper, 2 for scissor: "))
if ui==1:
    print("rock")
elif ui==2:
    print("Paper")
else:
    print("scissor")
ci=random.randint(0,2)
if ci==1:
    print("rock")
elif ci==2:
    print("Paper")
else:
    print("scissor")
    
if ci==ui:
    print("Draw")
elif ui<ci:
    print("you lost")
elif ci<ui:
    print("you win")
elif ui==0 and ci==2:
    print("you win")
elif ui==2 and ci==0:
    print("You lost")
else:
    print("Invalid")


# In[ ]:




