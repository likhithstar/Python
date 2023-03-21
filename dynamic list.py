#!/usr/bin/env python
# coding: utf-8

# In[4]:


l=[]
a = int(input("Enter size of a list: "))

for i in range(1,a+1):
    
    b = input("Enter element name: ")
    
    l.insert(i-1,b)
print(l)

