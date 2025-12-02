#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()


# In[9]:


n=5
for i in range(1,n+1):
        print(("*"*i)+((n-i)*" "))


# In[16]:


n=5
for i in range(n,0,-1):
        print(("*"*i)+((n-i)*" "))


# In[17]:


n=5
for i in range(n,0,-1):
        print(((n-i)*" ")+("*"*i))


# In[18]:


n=5
for i in range(1,n+1):
        print(((n-i)*" ")+("*"*i))


# In[28]:


n=5
for i in range(n,0,-1):
        print(("*"*i)+(2*(n-i)*" ")+("*"*i))
for i in range(1,n+1):
        print(("*"*i)+(2*(n-i)*" ")+("*"*i))


# In[29]:


n=5
for i in range(1,n+1):
        print(("*"*i)+(2*(n-i)*" ")+("*"*i))
for i in range(n-1,0,-1):
        print(("*"*i)+(2*(n-i)*" ")+("*"*i))


# In[30]:


n=5
for i in range(1,n+1):
        


# In[53]:


n=5
for i in range(1,n+1):
        print(((n-i)*" ")+("*"*i*2))


# In[62]:


n=5
for i in range(1,n):
        for k in range(n-i):
            print(" ",end="")
        for j in range(1,i+1):
            print(j,end=" ")
        print()
for i in range(n,0,-1):
        for k in range(n-i):
            print(" ",end="")
        for j in range(1,i+1):
            print(j,end=" ")
        print()


# In[58]:


n=5
for i in range(1,n):
        for k in range(n-i):
            print(" ",end=" ")
        for j in range(1,i+1):
            print(j,end="")
        print()
for i in range(n,0,-1):
        for k in range(n-i):
            print(" ",end=" ")
        for j in range(1,i+1):
            print(j,end="")
        print()


# In[ ]:




