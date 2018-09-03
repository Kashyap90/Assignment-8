
# coding: utf-8

# In[7]:


# Consider a DataFrame df where there is an integer column {'X':[7, 2, 0, 3, 4, 2, 5, 0, 3, 4]} with new column 'Y'

import pandas as pd 

df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})

import numpy as np 

izero = np.r_[-1, (df['X'] == 0).nonzero()[0]]

izero


# In[9]:


idx = np.arange(len(df))
idx


# In[10]:


df['Y'] = idx - izero[np.searchsorted(izero - 1, idx) - 1]
df


# In[11]:


# Create a DatetimeIndex that contains each business day of 2015 and use it to index a Series of random numbers.

import pandas as pd
import numpy as np

dti = pd.date_range(start='2015-01-01', end='2015-12-31', freq='B') 
s = pd.Series(np.random.rand(len(dti)), index=dti)
dti


# In[12]:


# Find the sum of the values in s for every Wednesday

s[s.index.weekday ==2].sum()


# In[13]:


# Average For each calendar month

s.resample('M').mean()


# In[14]:


# For each group of four consecutive calendar months in s, find the date on which the highest value occurred.

s.groupby(pd.Grouper(freq='4M')).idxmax()

