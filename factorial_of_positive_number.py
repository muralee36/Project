#!/usr/bin/env python
# coding: utf-8

# In[9]:


#my 4th project
#program to find the factorial of a positive number
def factorial():
    number=int(input('enter the number to find factorial of : '))
    factorial=1
    if number==0:
        factorial=1
    elif number>0:
        for x in range(1,number+1):
            factorial*=x
    else:
        return 'invalid value'
    return factorial
factorial()

