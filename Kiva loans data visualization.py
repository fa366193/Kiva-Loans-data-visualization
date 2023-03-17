#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


# In[3]:


#Creating table by reading CSV 
df = pd.read_csv("Desktop/kiva_loans.csv")
df.head()


# In[4]:


#Plotting loan amount per country
f, ax = plt.subplots(figsize=(15, 10))
sns.barplot(data=df, x='country', y='loan_amount')


# In[9]:


# Box Plot by Activity
plt.figure(figsize=(16, 10))
sns.boxplot(data=df, x="activity", y="loan_amount")


# In[10]:


# Violin Plots
plt.figure(figsize=(16, 10))
sns.violinplot(data=df, x="activity", y="loan_amount")

plt.figure(figsize=(16, 10))
sns.violinplot(data=df, x="country", y="loan_amount")


# In[ ]:




