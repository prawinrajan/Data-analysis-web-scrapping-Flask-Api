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
HTML(dataset.head().to_html())


# In[3]:


# Name of the Unique departments
dataset.Department.unique()


# In[4]:


#Department Vs Monthly rating


# In[5]:


df = DataFrame(dict(
    Department=dataset.Department,
    MonthlyRate=dataset.MonthlyRate
    ))


# In[6]:


df.head()


# In[7]:


column_MonthlyRate=df['MonthlyRate']
maxcolumn_MonthlyRate=column_MonthlyRate.max()
mincolumn_MonthlyRate=column_MonthlyRate.min()
avgcolumn_MonthlyRate=column_MonthlyRate.mean()
print("max monthly rate",maxcolumn_MonthlyRate)
print("min monthly rate",mincolumn_MonthlyRate)
print("avg monthly rate",avgcolumn_MonthlyRate)


# In[8]:


#Monthly Rate
print("---------------Research & Development---------------------")

MaxMonthlyRate_in_RESEARCHandDEV=df[(df.Department == "Research & Development") & (df.MonthlyRate == maxcolumn_MonthlyRate)]
#count of records
Total_max_count_of_MonthlyRate_in_RESEARCHandDEV = len(MaxMonthlyRate_in_RESEARCHandDEV.axes[0])
print("Max MonthlyRate by Reserch",Total_max_count_of_MonthlyRate_in_RESEARCHandDEV)

#min
MinMonthlyRate_in_RESEARCHandDEV=df[(df.Department == "Research & Development") & (df.MonthlyRate == mincolumn_MonthlyRate)]
#count of records
Total_min_count_of_MonthlyRate_in_RESEARCHandDEV = len(MinMonthlyRate_in_RESEARCHandDEV.axes[0])
print("min MonthlyRate by Reserch",Total_min_count_of_MonthlyRate_in_RESEARCHandDEV)

#above_avg
above_avg_MonthlyRate_in_RESEARCHandDEV=df[(df.Department == "Research & Development") & (df.MonthlyRate >avgcolumn_MonthlyRate)]
#count of records
Total_above_avg_count_of_MonthlyRate_in_RESEARCHandDEV = len(above_avg_MonthlyRate_in_RESEARCHandDEV.axes[0])
print("above avg MonthlyRate by Reserch",Total_above_avg_count_of_MonthlyRate_in_RESEARCHandDEV)

#below_avg
below_avg_MonthlyRate_in_RESEARCHandDEV=df[(df.Department == "Research & Development") & (df.MonthlyRate < avgcolumn_MonthlyRate)]
#count of records
Total_below_avg_count_of_MonthlyRate_in_RESEARCHandDEV = len(below_avg_MonthlyRate_in_RESEARCHandDEV.axes[0])
print("below avg MonthlyRate by Reserch",Total_below_avg_count_of_MonthlyRate_in_RESEARCHandDEV)


# In[9]:


#Monthly Rate
print("---------------Sales---------------------")

MaxMonthlyRate_in_Sales=df[(df.Department == "Sales") & (df.MonthlyRate == maxcolumn_MonthlyRate)]
#count of records
Total_max_count_of_MonthlyRate_in_Sales = len(MaxMonthlyRate_in_Sales.axes[0])
print("Max MonthlyRate by Sales",Total_max_count_of_MonthlyRate_in_Sales)

#min
MinMonthlyRate_in_Sales=df[(df.Department == "Sales") & (df.MonthlyRate == mincolumn_MonthlyRate)]
#count of records
Total_min_count_of_MonthlyRate_in_Sales= len(MinMonthlyRate_in_Sales.axes[0])
print("min MonthlyRate by Sales",Total_min_count_of_MonthlyRate_in_Sales)

#above_avg
above_avg_MonthlyRate_in_Sales=df[(df.Department == "Sales") & (df.MonthlyRate >avgcolumn_MonthlyRate)]
#count of records
Total_above_avg_count_of_MonthlyRate_in_Sales = len(above_avg_MonthlyRate_in_Sales.axes[0])
print("above avg MonthlyRate by Sales",Total_above_avg_count_of_MonthlyRate_in_Sales)

#below_avg
below_avg_MonthlyRate_in_Sales=df[(df.Department == "Sales") & (df.MonthlyRate < avgcolumn_MonthlyRate)]
#count of records
Total_below_avg_count_of_MonthlyRate_in_Sales = len(below_avg_MonthlyRate_in_Sales.axes[0])
print("below avg MonthlyRate by Sales",Total_below_avg_count_of_MonthlyRate_in_Sales)


# In[10]:


#Monthly Rate
print("---------------Human Resources---------------------")
#HumanResources
MaxMonthlyRate_in_HumanResources=df[(df.Department == "Human Resources") & (df.MonthlyRate == maxcolumn_MonthlyRate)]
#count of records
Total_max_count_of_MonthlyRate_in_HumanResources = len(MaxMonthlyRate_in_HumanResources.axes[0])
print("Max MonthlyRate by Human Resources",Total_max_count_of_MonthlyRate_in_HumanResources)

#min
MinMonthlyRate_in_HumanResources=df[(df.Department == "Human Resources") & (df.MonthlyRate == mincolumn_MonthlyRate)]
#count of records
Total_min_count_of_MonthlyRate_in_HumanResources= len(MinMonthlyRate_in_HumanResources.axes[0])
print("min MonthlyRate by Human Resources",Total_min_count_of_MonthlyRate_in_HumanResources)

#above_avg
above_avg_MonthlyRate_in_HumanResources=df[(df.Department == "Human Resources") & (df.MonthlyRate >avgcolumn_MonthlyRate)]
#count of records
Total_above_avg_count_of_MonthlyRate_in_HumanResources = len(above_avg_MonthlyRate_in_HumanResources.axes[0])
print("above avg MonthlyRate by Human Resources",Total_above_avg_count_of_MonthlyRate_in_HumanResources)

#below_avg
below_avg_MonthlyRate_in_HumanResources=df[(df.Department == "Human Resources") & (df.MonthlyRate < avgcolumn_MonthlyRate)]
#count of records
Total_below_avg_count_of_MonthlyRate_in_HumanResources = len(below_avg_MonthlyRate_in_HumanResources.axes[0])
print("below avg MonthlyRate by Human Resources",Total_below_avg_count_of_MonthlyRate_in_HumanResources)


# In[13]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['Max', 'min','above avg','below avg']
Research_and_Development = [Total_max_count_of_MonthlyRate_in_RESEARCHandDEV,
Total_min_count_of_MonthlyRate_in_RESEARCHandDEV,
Total_above_avg_count_of_MonthlyRate_in_RESEARCHandDEV,
Total_below_avg_count_of_MonthlyRate_in_RESEARCHandDEV]

Sales = [Total_max_count_of_MonthlyRate_in_Sales,
Total_min_count_of_MonthlyRate_in_Sales,
Total_above_avg_count_of_MonthlyRate_in_Sales,
Total_below_avg_count_of_MonthlyRate_in_Sales]

Human_Resources=[Total_max_count_of_MonthlyRate_in_HumanResources,
Total_min_count_of_MonthlyRate_in_HumanResources,
Total_above_avg_count_of_MonthlyRate_in_HumanResources,
Total_below_avg_count_of_MonthlyRate_in_HumanResources]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, Research_and_Development, width, label='Research & Development')
rects2 = ax.bar(x + width/2, Sales, width, label='Sales')
rects3 = ax.bar(x + width*1.5, Human_Resources, width, label='Human_Resources')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Monthlyrating')
ax.set_title('Department Vs Monthlyrating')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
             
fig.tight_layout()
plt.savefig('DepartmentVSMonthlyRateing.pdf') 
plt.show()


# In[ ]:




