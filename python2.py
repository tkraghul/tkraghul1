#!/usr/bin/env python
# coding: utf-8

# In[1]:


rows = 5




# In[4]:


for i in range(rows):
    for j in range(i + 1):
        print("*", end=" ")
    print()

for i in range(rows - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


# In[ ]:




