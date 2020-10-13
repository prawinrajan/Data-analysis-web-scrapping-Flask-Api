#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
from IPython.display import HTML
import numpy as np


# In[2]:


#read data
dataset = pd.read_csv('/home/prawin/employee .csv')


# In[3]:


HTML(dataset.head().to_html())


# In[4]:


# Name of the Unique departments
dataset.Department.unique()


# In[5]:


HTML(dataset.groupby('Department').describe().to_html())


# In[6]:


from pandas import Series, DataFrame, Panel


# In[7]:


df = DataFrame(dict(
    Department=dataset.Department,
    DailyRate=dataset.DailyRate,
    HourlyRate=dataset.HourlyRate,
    JobInvolvement=dataset.JobInvolvement,
    MonthlyRate=dataset.MonthlyRate,
    OverTime=dataset.OverTime,
    PerformanceRating=dataset.PerformanceRating,
    StandardHours=dataset.StandardHours
    ))


# In[8]:


HTML(df.to_html())


# In[9]:


df[df.Department=='Sales']


# In[10]:


#number of employees belong to Department=sales
df.query('Department == "Sales"').Department.count()


# In[11]:


#number of employees belong to Department=Research & Development
df.query('Department == "Research & Development"').Department.count()


# In[12]:


#number of employees belong to Department=Human Resources
df.query('Department == "Human Resources"').Department.count()


# In[13]:


#which department has High JOb invlovesment 
df = DataFrame(dict(
    Department=dataset.Department,
    JobInvolvement=dataset.JobInvolvement
    ))


# In[14]:


df


# In[15]:


column = df["JobInvolvement"]


# In[16]:


#high job JobInvolvement value
maxJobInvolement=column.max()


# In[17]:


#Research & dev department, how many of them has high job JobInvolvement
high_jobInvolvement_in_RESEARCHandDEV=df[(df.Department == "Research & Development") & (df.JobInvolvement == maxJobInvolement)]


# In[18]:


#HTML(high_jobInvolvement_in_RESEARCHandDEV.to_html())


# In[19]:


#count of records
Total_count_in_RESEARCHandDEV = len(high_jobInvolvement_in_RESEARCHandDEV.axes[0])
Total_count_in_RESEARCHandDEV


# In[20]:


#Sales department, how many of them has high job JobInvolvement
high_jobInvolvement_in_Sales=df[(df.Department == "Sales") & (df.JobInvolvement == maxJobInvolement)]


# In[21]:


#count of records
Total_count_in_Sales = len(high_jobInvolvement_in_Sales.axes[0])
Total_count_in_Sales


# In[22]:


#Human Resources department, how many of them has high job JobInvolvement
high_jobInvolvement_in_Human_Resources=df[(df.Department == "Human Resources") & (df.JobInvolvement == maxJobInvolement)]


# In[23]:


#count of records
Total_count_in_HumanResources = len(high_jobInvolvement_in_Human_Resources.axes[0])
Total_count_in_HumanResources


# In[24]:


#which department has High Job invloement employees
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
dep = ['Research_and_dev', 'Sales', 'HumanResources']
max_involement_emp_count = [Total_count_in_RESEARCHandDEV,Total_count_in_Sales,Total_count_in_HumanResources]
ax.bar(dep,max_involement_emp_count)
ax.set_ylabel('Scores')
ax.set_title('Comparison between Research_and_dev, Sales, HumanResources based High Job invloement employees')

plt.show()


# In[25]:


#which department has High HourlyRate
df = DataFrame(dict(
    Department=dataset.Department,
    HourlyRate=dataset.HourlyRate
    ))


# In[26]:


df


# In[27]:


select_HourlyRate_col= df["HourlyRate"]


# In[28]:


#Max hourly rate
Max_hourly_rate=select_HourlyRate_col.max()


# In[29]:


Max_hourly_rate


# In[30]:


select_HourlyRate_col.plot()


# In[31]:


#Research & dev department, how many of them has Maxhourlyrate
Maxhourlyrate_in_RESEARCHandDEV=df[(df.Department == "Research & Development") & (df.HourlyRate == Max_hourly_rate)]

#count of records
Total_count_of_hourlyrate_in_RESEARCHandDEV = len(Maxhourlyrate_in_RESEARCHandDEV.axes[0])
Total_count_of_hourlyrate_in_RESEARCHandDEV


# In[32]:


#Sales, how many of them has Maxhourlyrate
Maxhourlyrate_in_Sales=df[(df.Department == "Sales") & (df.HourlyRate == Max_hourly_rate)]

#count of records
Total_count_of_hourlyrate_in_Sales = len(Maxhourlyrate_in_Sales.axes[0])
Total_count_of_hourlyrate_in_Sales


# In[33]:


#Human Resources, how many of them has Maxhourlyrate
Maxhourlyrate_in_HumanResources=df[(df.Department == "Human Resources") & (df.HourlyRate == Max_hourly_rate)]

#count of records
Total_count_of_hourlyrate_in_HumanResources = len(Maxhourlyrate_in_HumanResources.axes[0])
Total_count_of_hourlyrate_in_HumanResources


# In[34]:


#which department working More hours
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
dep = ['Research_and_dev', 'Sales', 'HumanResources']
Max_working_hours = [Total_count_of_hourlyrate_in_RESEARCHandDEV,Total_count_of_hourlyrate_in_Sales,Total_count_of_hourlyrate_in_HumanResources]
ax.bar(dep,Max_working_hours)
ax.set_ylabel('Scores')
ax.set_title('Comparison between Research_and_dev, Sales, HumanResources based on working hours')
plt.show()


# In[35]:


#which department has High DailyRate,
df = DataFrame(dict(
    Department=dataset.Department,
    DailyRate=dataset.DailyRate,
    MonthlyRate=dataset.MonthlyRate,
    OverTime=dataset.OverTime,
    PerformanceRating=dataset.PerformanceRating
    ))


# In[36]:


column_DailyRate= df["DailyRate"]
#high job JobInvolvement value
Max_column_DailyRate=column_DailyRate.max()
Max_column_DailyRate

column_MonthlyRate= df["MonthlyRate"]
max_column_MonthlyRate=column_MonthlyRate.max()
max_column_MonthlyRate


column_PerformanceRating= df["PerformanceRating"]
max_column_PerformanceRating=column_PerformanceRating.max()
max_column_PerformanceRating


# In[37]:


#Research & dev department, how many of them has Dailyrate
MaxDailyRate_in_RESEARCHandDEV=df[(df.Department == "Research & Development") & (df.DailyRate == Max_column_DailyRate)]
print("Research & dev department")
#count of records
Total_count_of_Dailyrate_in_RESEARCHandDEV = len(MaxDailyRate_in_RESEARCHandDEV.axes[0])
print("dailyrate",Total_count_of_Dailyrate_in_RESEARCHandDEV)

#Research & dev department, how many of them has MonthlyRate
MaxMonthlyRate_in_RESEARCHandDEV=df[(df.Department == "Research & Development") & (df.MonthlyRate == max_column_MonthlyRate)]
#count of records
Total_count_of_MonthlyRate_in_RESEARCHandDEV = len(MaxDailyRate_in_RESEARCHandDEV.axes[0])
print("MonthlyRate",Total_count_of_MonthlyRate_in_RESEARCHandDEV)

#Research & dev department, how many of them has OverTime
MaxOverTime_in_RESEARCHandDEV=df[(df.Department == "Research & Development") & (df.OverTime == 'Yes')]
#count of records
Total_count_of_OverTime_in_RESEARCHandDEV = len(MaxOverTime_in_RESEARCHandDEV.axes[0])
print("OverTime",Total_count_of_OverTime_in_RESEARCHandDEV)

#Research & dev department, how many of them has PerformanceRating
MaxPerformanceRating_in_RESEARCHandDEV=df[(df.Department == "Research & Development") & (df.PerformanceRating == max_column_PerformanceRating)]
#count of records
Total_count_of_PerformanceRating_in_RESEARCHandDEV = len(MaxPerformanceRating_in_RESEARCHandDEV.axes[0])
print("PerformanceRating",Total_count_of_PerformanceRating_in_RESEARCHandDEV)


# In[38]:


#Sales, how many of them has Dailyrate
MaxDailyRate_in_Sales=df[(df.Department == "Sales") & (df.DailyRate == Max_column_DailyRate)]
print("Sales")
#count of records
Total_count_of_Dailyrate_in_Sales = len(MaxDailyRate_in_Sales.axes[0])
print("dailyrate",Total_count_of_Dailyrate_in_Sales)

#Research & dev department, how many of them has MonthlyRate
MaxMonthlyRate_in_Sales=df[(df.Department == "Sales") & (df.MonthlyRate == max_column_MonthlyRate)]
#count of records
Total_count_of_MonthlyRate_in_Sales = len(MaxMonthlyRate_in_Sales.axes[0])
print("MonthlyRate",Total_count_of_MonthlyRate_in_Sales)

#Research & dev department, how many of them has OverTime
MaxOverTime_in_Sales=df[(df.Department == "Sales") & (df.OverTime == 'Yes')]
#count of records
Total_count_of_OverTime_in_Sales = len(MaxOverTime_in_Sales.axes[0])
print("OverTime",Total_count_of_OverTime_in_Sales)

#Research & dev department, how many of them has PerformanceRating
MaxPerformanceRating_in_Sales=df[(df.Department == "Sales") & (df.PerformanceRating == max_column_PerformanceRating)]
#count of records
Total_count_of_PerformanceRating_in_Sales = len(MaxPerformanceRating_in_Sales.axes[0])
print("PerformanceRating",Total_count_of_PerformanceRating_in_Sales)


# In[39]:


# HumanResources, how many of them has Dailyrate
MaxDailyRate_in_HumanResources=df[(df.Department == "Human Resources") & (df.DailyRate == Max_column_DailyRate)]
print("HumanResources")
#count of records
Total_count_of_Dailyrate_in_HumanResources = len(MaxDailyRate_in_HumanResources.axes[0])
print("dailyrate",Total_count_of_Dailyrate_in_HumanResources)

#Research & dev department, how many of them has MonthlyRate
MaxMonthlyRate_in_HumanResources=df[(df.Department == "Human Resources") & (df.MonthlyRate == max_column_MonthlyRate)]
#count of records
Total_count_of_MonthlyRate_in_HumanResources = len(MaxMonthlyRate_in_HumanResources.axes[0])
print("MonthlyRate",Total_count_of_MonthlyRate_in_HumanResources)

#Research & dev department, how many of them has OverTime
MaxOverTime_in_HumanResources=df[(df.Department == "Human Resources") & (df.OverTime == 'Yes')]
#count of records
Total_count_of_OverTime_in_HumanResources = len(MaxOverTime_in_HumanResources.axes[0])
print("OverTime",Total_count_of_OverTime_in_HumanResources)

#Research & dev department, how many of them has PerformanceRating
MaxPerformanceRating_in_HumanResources=df[(df.Department == "Human Resources") & (df.PerformanceRating == max_column_PerformanceRating)]
#count of records
Total_count_of_PerformanceRating_in_HumanResources = len(MaxPerformanceRating_in_HumanResources.axes[0])
print("PerformanceRating",Total_count_of_PerformanceRating_in_HumanResources)


# In[41]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['Dailyrate', 'Monthlyrate', 'OverTime', 'PerformanceRating']
research_and_dev = [Total_count_of_Dailyrate_in_RESEARCHandDEV,
         Total_count_of_MonthlyRate_in_RESEARCHandDEV,Total_count_of_OverTime_in_RESEARCHandDEV,
         Total_count_of_PerformanceRating_in_RESEARCHandDEV]

Sales = [Total_count_of_Dailyrate_in_Sales,
         Total_count_of_MonthlyRate_in_Sales,
         Total_count_of_OverTime_in_Sales,
         Total_count_of_PerformanceRating_in_Sales]
Human_resource=[Total_count_of_Dailyrate_in_HumanResources, 
         Total_count_of_MonthlyRate_in_HumanResources,
         Total_count_of_OverTime_in_HumanResources, 
        Total_count_of_PerformanceRating_in_HumanResources]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, research_and_dev, width, label='research_and_dev')
rects2 = ax.bar(x + width/2, Sales, width, label='Sales')
rects3 = ax.bar(x + width*1.5, Human_resource, width, label='Human_resource')



# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Comparison between HourlyRate, MonthlyRate,OverTime, perfomanceRate')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 4, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
fig.tight_layout()

plt.rcParams["figure.figsize"] = (10, 5)
plt.show()


# In[ ]:




