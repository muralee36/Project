#!/usr/bin/env python
# coding: utf-8

# In[18]:


#my 5th Project
#mortgage calculator with user deciding the compounding interval
#monthly,weekly,daily,continually
def mortgage():
    loan=float(input('Enter the amount needed : '))
    rate=float(input('Enter the yearly rate for the amount : '))
    time=float(input('Enter the time required for loan payback : '))
    pay_mode=input('Enter the mode of payment :\n M for monthly payments\n W for weekly payments\n D for daily payments\n :')
    #no of payments = n
    if pay_mode=='M' or pay_mode== 'm':
        n=12
        mode='Monthly'
    elif pay_mode== 'W' or pay_mode=='w':
        n=52
        mode='Monthly'
    else:
        n=365
        mode='Daily'
    # no = no of payments
    no=n*time
    #c= interest rate
    c=rate/(100*n)
    m=(1+c)**no
    amount=loan*((c*m)/(m-1))
    print(f'An amount of Rs {amount:.2f} is to be paid {mode} \nTotal amount payable after {time} years : {amount*n*time:.2f}')
mortgage()


# In[8]:





# In[11]:





# In[ ]:




