#!/usr/bin/env python
# coding: utf-8

# In[1]:


#my second project
#Prime Factors of a given number


# In[4]:


#function to find factors of a number

def find_factors(number):
    factors=[]
    for i in range(1,number+1):
        if(number%i==0):
            factors.append(i)
    return factors

#function to check for prime

def prime_no_check(number):
    while number>1:
        for i in range(2,number):
            if(number%i)==0:
                return False
        else:
            return True
    else:
        return True
    
#function to find prime factors

def prime_factors(number):
    factors=find_factors(number)
    req_factors=factors[1:len(factors)-1]
    prime_factors=[]
    for i in req_factors:
        if prime_no_check(i):
            prime_factors.append(i)
    return prime_factors
number=int(input('Enter the number to find Prime Factors of : '))
print(f'The prime factors of {number} are : {prime_factors(number)}')


# In[ ]:





# In[ ]:




