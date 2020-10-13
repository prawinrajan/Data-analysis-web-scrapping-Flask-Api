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


# In[3]:


HTML(dataset.head().to_html())


# In[4]:


# Name of the Unique departments
dataset.EducationField.unique()


# In[5]:


df = DataFrame(dict(
    EducationField=dataset.EducationField,
    HourlyRate=dataset.HourlyRate,
    JobRole=dataset.JobRole,
    PerformanceRating=dataset.PerformanceRating,
    ))


# In[6]:


#which categorie pepoles working more hours
HourlyRatecolumn = df["HourlyRate"]
#max hourlyrate 
maxHourlyRatecolumn=HourlyRatecolumn.max()
maxHourlyRatecolumn


# In[7]:


# Life Sciences, which category pepoles working long time
print("Hourly rate")
high_ourly_rate_in_Life_Sciences=df[(df.EducationField == "Life Sciences") & (df.HourlyRate == maxHourlyRatecolumn)]
#count of records
Total_countof_hourlyRate_in_LifeSciences= len(high_ourly_rate_in_Life_Sciences.axes[0])
print("Life science",Total_countof_hourlyRate_in_LifeSciences)

high_ourly_rate_in_Other=df[(df.EducationField == "Other") & (df.HourlyRate == maxHourlyRatecolumn)]
#count of records
Total_countof_hourlyRate_in_Other= len(high_ourly_rate_in_Other.axes[0])
print("Other",Total_countof_hourlyRate_in_Other)


high_ourly_rate_in_Medical=df[(df.EducationField == "Medical") & (df.HourlyRate == maxHourlyRatecolumn)]
#count of records
Total_countof_hourlyRate_in_Medical= len(high_ourly_rate_in_Medical.axes[0])
print("Medical",Total_countof_hourlyRate_in_Medical)

high_ourly_rate_in_Marketing=df[(df.EducationField == "Marketing") & (df.HourlyRate == maxHourlyRatecolumn)]
#count of records
Total_countof_hourlyRate_in_Marketing= len(high_ourly_rate_in_Marketing.axes[0])
print("Marketing",Total_countof_hourlyRate_in_Marketing)

high_ourly_rate_in_Technical_Degree=df[(df.EducationField == "Technical Degree") & (df.HourlyRate == maxHourlyRatecolumn)]
#count of records
Total_countof_hourlyRate_in_Technical_Degree= len(high_ourly_rate_in_Technical_Degree.axes[0])
print("Technical Degree",Total_countof_hourlyRate_in_Technical_Degree)

high_ourly_rate_in_Human_Resources=df[(df.EducationField == "Human Resources") & (df.HourlyRate == maxHourlyRatecolumn)]
#count of records
Total_countof_hourlyRate_in_Human_Resources= len(high_ourly_rate_in_Human_Resources.axes[0])
print("Human Resources",Total_countof_hourlyRate_in_Human_Resources)


# In[8]:


#which categorie pepoles working more hours
PerformanceRatingcolumn = df["PerformanceRating"]
#max hourlyrate 
maxPerformanceRatingcolumn=PerformanceRatingcolumn.max()
maxPerformanceRatingcolumn


# In[9]:


# Life Sciences, which category pepoles working long time
print("PerformanceRating")
PerformanceRating_in_Life_Sciences=df[(df.EducationField == "Life Sciences") & (df.PerformanceRating == maxPerformanceRatingcolumn)]
#count of records
Total_countof_PerformanceRating_in_LifeSciences= len(PerformanceRating_in_Life_Sciences.axes[0])
print("Life science",Total_countof_PerformanceRating_in_LifeSciences)

PerformanceRating_in_Other=df[(df.EducationField == "Other") & (df.PerformanceRating == maxPerformanceRatingcolumn)]
#count of records
Total_countof_PerformanceRating_in_Other= len(PerformanceRating_in_Other.axes[0])
print("Other",Total_countof_PerformanceRating_in_Other)


PerformanceRating_rate_in_Medical=df[(df.EducationField == "Medical") & (df.PerformanceRating == maxPerformanceRatingcolumn)]
#count of records
Total_countof_PerformanceRating_in_Medical= len(PerformanceRating_rate_in_Medical.axes[0])
print("Medical",Total_countof_PerformanceRating_in_Medical)

PerformanceRating_in_Marketing=df[(df.EducationField == "Marketing") & (df.PerformanceRating == maxPerformanceRatingcolumn)]
#count of records
Total_countof_PerformanceRating_in_Marketing= len(PerformanceRating_in_Marketing.axes[0])
print("Marketing",Total_countof_PerformanceRating_in_Marketing)

PerformanceRating_in_Technical_Degree=df[(df.EducationField == "Technical Degree") & (df.PerformanceRating == maxPerformanceRatingcolumn)]
#count of records
Total_countof_PerformanceRatingin_Technical_Degree= len(PerformanceRating_in_Technical_Degree.axes[0])
print("Technical Degree",Total_countof_PerformanceRatingin_Technical_Degree)

PerformanceRating_in_Human_Resources=df[(df.EducationField == "Human Resources") & (df.PerformanceRating == maxPerformanceRatingcolumn)]
#count of records
Total_countof_PerformanceRating_in_Human_Resources= len(PerformanceRating_in_Human_Resources.axes[0])
print("Human Resources",Total_countof_PerformanceRating_in_Human_Resources)


# In[11]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['Life science', 'Other','Medical','Marketing','Technical Degree','Human Resources']
HourlyRate = [Total_countof_hourlyRate_in_LifeSciences,
              Total_countof_hourlyRate_in_Other,
              Total_countof_hourlyRate_in_Medical,
              Total_countof_hourlyRate_in_Marketing,
              Total_countof_hourlyRate_in_Technical_Degree,
              Total_countof_hourlyRate_in_Human_Resources]

PerformanceRating = [Total_countof_PerformanceRating_in_LifeSciences,
              Total_countof_PerformanceRating_in_Other,
              Total_countof_PerformanceRating_in_Medical,
              Total_countof_PerformanceRating_in_Marketing,
              Total_countof_PerformanceRatingin_Technical_Degree,
              Total_countof_PerformanceRating_in_Human_Resources]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, HourlyRate, width, label='HourlyRate')
rects2 = ax.bar(x + width/2, PerformanceRating, width, label='PerformanceRating')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('rating')
ax.set_title('comparison of Hourlyrating and PerformanceRating based on education field')
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

fig.tight_layout()
plt.savefig('which_backgroung_pepoles_working_efficiently.pdf') 
plt.show()


# In[ ]:




