#!/usr/bin/env python
# coding: utf-8

# In[2]:


#String Basics
len('Mera Bharath Mahaan')


# In[4]:


len("MeraBharathMahaan")


# In[5]:


#String Indexing
print('Mera Bharath Mahaan')


# In[6]:


# Assign s as a string
s = 'Mera Bharath Mahaan'


# In[7]:


s


# In[8]:


S = 'Jai Ho Bharath'
print(S)


# In[9]:


s


# In[10]:


s[0]


# In[11]:


s[1]


# In[12]:


s[2]


# In[13]:


s[1:]


# In[14]:


s[:3]


# In[15]:


s[3:6]


# In[16]:


s[:]


# In[17]:


s[-1]


# In[18]:


s[:-1]


# In[19]:


s[-1:]


# In[20]:


s[::1]


# In[21]:


s[::2]


# In[22]:


s[::-1]


# In[23]:


##String Properties
s
s[0] = 'x'


# In[24]:


s


# In[25]:


s + ' Namasthe!'


# In[26]:


s


# In[27]:


#s = 'Mera Bharath Mahaan '
s = 'Hamara' + s[4:]
s


# In[28]:


# We can reassign s completely though!
s = s + ' Namasthe!'
print(s)


# In[29]:


letter = 'z'
letter*10


# In[30]:


#Basic Built-in String methods
s = 'Mera Bharath Mahaan'
# Upper Case a string
s.upper()


# In[31]:


# Lower case
s.lower()


# In[32]:


s.Split()


# In[33]:


s.split('a')


# In[34]:


s.split('ha')


# In[35]:


s.split('Ha')


# In[36]:


s = 'Mera Bharath! #Mahaan'
s.split()


# In[37]:


s.split('#')


# In[ ]:




