#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance as yf
import numpy as np


# In[2]:


import pandas as pd


# In[17]:


from matplotlib import pyplot as plt


# In[7]:


nifty_data = pd.read_csv("Nifty50.csv")


# In[8]:


nifty_daily_returns = nifty_data["Close"].pct_change()[1:]


# In[9]:


nifty_standard_deviation = nifty_daily_returns.std()


# In[11]:


nifty_mean = np.mean(nifty_daily_returns)


# In[13]:


nifty_standard_deviation


# In[22]:


mean_returns = []
for k in range(100):
    mean_returns.append(np.mean(np.random.normal(nifty_mean, nifty_standard_deviation, size = len(nifty_data))))
        


# In[32]:


num_bins = 10
bin_range = (np.min(mean_returns), np.max(mean_returns))
bin_counts, bin_edges = np.histogram(mean_returns, bins=num_bins, range=bin_range)
bar_positions = np.arange(num_bins)
plt.bar(bar_positions, bin_counts, align='center')
plt.xlabel('Bins')
plt.ylabel('Frequency')
plt.title('Binned Bar Plot')
bin_labels = [round(np.min(mean_returns) + (i/10)*(np.max(mean_returns) - np.min(mean_returns)), 4) for i in range(num_bins)]
plt.xticks(bar_positions, bin_labels)
plt.show()


# In[ ]:




