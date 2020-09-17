#!/usr/bin/env python
# coding: utf-8

# In[1]:


#my first project


# In[4]:


#Fibonacci series upto n terms


# In[5]:


# x is the n-2 term ,y is the n-1 term and z is the nth term


# In[14]:


n=int(input('enter the length(>1) of the fibonacci series : '))
x=0
y=1
z=0
fibonacci_series=[0,1]


# In[15]:


while(len(fibonacci_series)<n):
    z=x+y
    x=y
    y=z
    fibonacci_series.append(z)
print(f'The Fibonacci series upto {n} terms is : ')
print(fibonacci_series)


# In[ ]:




