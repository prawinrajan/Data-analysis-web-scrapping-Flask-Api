#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
from IPython.display import HTML
import numpy as np

from pandas import Series, DataFrame, Panel


# In[2]:


#read data
dataset = pd.read_csv('/home/prawin/employee .csv')


# In[5]:


dataset.head()


# In[20]:


df = DataFrame(dict(
    Age=dataset.Age,
    HourlyRate=dataset.HourlyRate
    ))


# In[23]:


age=df['Age']
maxage=age.max()
minage=age.min()
avgAge=age.mean()

print("max age",maxage)
print("min age",minage)
print("avg age",avgAge)


# In[27]:


HourlyRate=df['HourlyRate']
maxHourlyRate=HourlyRate.max()
minHourlyRate=HourlyRate.min()
avgHourlyRate=HourlyRate.mean()

print("max HourlyRate",maxHourlyRate)
print("min HourlyRate",minHourlyRate)
print("avg HourlyRate",avgHourlyRate)


# In[52]:


# Age min and working hour is above avg.
Age_min=df[(df.HourlyRate > avgHourlyRate) & (df.Age > minage)]
#count of records
toatl_Age_min = len(Age_min.axes[0])
print("toatl_Age_min",toatl_Age_min)

# Age above avg and working hour is less than avg hour rate
age_above_avg=df[(df.HourlyRate < avgHourlyRate) & (df.Age < avgAge)]
#count of records
TotalRow_has_age_above_avg = len(age_above_avg.axes[0])
print("TotalRow_has_age_above_avg",TotalRow_has_age_above_avg)

#age below avg and working hours greater than min Hourlyrate
age_below_avg=df[(df.HourlyRate > minHourlyRate) & (df.Age < avgAge)]
TotalRow_has_age_below_avg = len(age_below_avg.axes[0])
print("TotalRow_has_age_below_avg",TotalRow_has_age_below_avg)


# In[61]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('ggplot')

x = ['Age_min and \n working hour greater\nthan avg', 'age less than above avg \n and working hour less than\n avg', 'age below avg and\n working hour greater\n than min hourly rate']

data=[toatl_Age_min,TotalRow_has_age_above_avg,TotalRow_has_age_below_avg]

x_pos = [i for i, _ in enumerate(x)]

plt.rcParams["figure.figsize"] = (8, 4)

plt.bar(x_pos, data, color='green')
plt.xlabel("Age VS HourlyRate")
plt.ylabel("count of employees")
plt.title("analysis working hours")

plt.xticks(x_pos, x)

plt.show()


# In[ ]:




