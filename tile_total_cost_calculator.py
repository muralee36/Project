#!/usr/bin/env python
# coding: utf-8

# In[8]:


#my third project
#tile total cost calculator
# a function tile_cost is created where input like W*H and cost are taken from the user
def tile_cost():
    width=int(input('enter the width of the floor (m) : '))
    height=int(input('enter the height of the floor (m) : '))
    cost_per_area=int(input('enter the cost per area (m^2) of tile : '))
    total_floor_area=width*height
    total_cost=cost_per_area*total_floor_area
    print( f'The total cost to cover {total_floor_area} square metre is : {total_cost}')


# In[9]:


tile_cost()


# In[ ]:




