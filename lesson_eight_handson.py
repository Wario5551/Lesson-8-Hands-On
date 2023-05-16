#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Here is how I import pandas into Jupyter notebook
import pandas as pd


# In[3]:


#This is how you make the dataset actually usable for commands
bison = pd.read_csv('/Users/wario5551/Downloads/BisonTracking.csv')


# In[23]:


#This is how I found the top 7 rows in the dataset
bison.head(7)


# In[6]:


#This is how I found the last 10 rows in the dataset
bison.tail(10)


# In[8]:


#This shows how many columns are in the dataset
len(bison.columns)


# In[9]:


#This shows how many rows are in the dataset
len(bison)


# In[12]:


#This is the standard deviation of length
bison.Length.std()


# In[13]:


#This is the mean of length
bison.Length.mean()


# In[20]:


#This commands shows how many of each bison specie is mentioned, there are
#a total of 633 that are antiquus
bison.Species.value_counts()


# In[21]:


#This is the median of length
bison.Length.median()


# In[ ]:




