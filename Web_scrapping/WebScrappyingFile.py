#!/usr/bin/env python
# coding: utf-8

# In[10]:


import requests
from bs4 import BeautifulSoup
import csv


# In[19]:


f = open('dataFile.csv', 'w',newline='')
fieldName=['URLs', 'Information Of the College', 'Courses and fees','Admission','review','department','Cut oFF']
thewriter=csv.DictWriter(f,fieldnames=fieldName)
thewriter.writeheader()


# In[20]:


basic_URL='https://collegedunia.com/btech-colleges'
Main_page=requests.get(basic_URL)
Main_soup = BeautifulSoup(Main_page.text,'html.parser')


# In[21]:


get_all_colleges_link=[]

for node in Main_soup.findAll('a',class_='college_name'):
    link=node["href"]
    get_all_colleges_link.append(node["href"])
    thewriter.writerow({'URLs':link})
    
    
get_all_colleges_link


# In[23]:


Info_of_college=[];Course_and_Fees=[];review=[];cutoff=[];department=[];admissionData=[]


# In[24]:


# Get Infomation and Departments of college
save_data=[]
def Info_and_Department(url):
    page=requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')
    rows=soup.find_all("div", class_="content-side")
    for row in rows:
        Info_of_college.append(row.get_text())
        thewriter.writerow({'Information Of the College':row.get_text()})
        
    department_row=soup.find_all("div",class_="courses")
    if department_row is None:
        department_row=soup.find_all("div",class_="cdcms_courses")
        if department_row is None:
            department_row=soup.find_all("div",class_="table")
            if department_row is None:
                department_row=""
            else:
                for row in department_row:
                    department.append(row.get_text())
                    thewriter.writerow({'department':row.get_text()})
        else:
            for row in department_row:
                department.append(row.get_text()) 
                thewriter.writerow({'department':row.get_text()})
    else:
        for row in department_row:
            department.append(row.get_text())
            thewriter.writerow({'department':row.get_text()})


# In[25]:


for i in get_all_colleges_link:
    Info_and_Department(i)


# In[26]:


# course and fee of college
def Course_and_Fee(url):
    page=requests.get(url+"/courses-fees")
    if page.status_code == 200:
        soup = BeautifulSoup(page.text,'html.parser')
        rows=soup.find_all("table", class_="table table-striped")
        for row in rows:
            Course_and_Fees.append(row.get_text())
            thewriter.writerow({'Courses and fees':row.get_text()})
            


# In[27]:


for CF in get_all_colleges_link:
    Course_and_Fee(CF)


# In[28]:


# admission of college

def DetailsOfAdmission(url):
    page=requests.get(url+"/admission")
    if page.status_code == 200:
        soup = BeautifulSoup(page.text,'html.parser')
        rows=soup.find_all("div", class_="content_body wrap_body")
        for row in rows:
            admissionData.append(row.get_text())
            thewriter.writerow({'Admission':row.get_text()})


# In[29]:


for admi in get_all_colleges_link:
    DetailsOfAdmission(admi)


# In[30]:


# Review of college
def ReviewDetails(url):
    page=requests.get(url+"/reviews")
    if page.status_code == 200:
        soup = BeautifulSoup(page.text,'html.parser')
        rows=soup.find_all("div", class_="content_body content_pad")
        for row in rows:
            review.append(row.get_text())
            thewriter.writerow({'review':row.get_text()})


# In[31]:


for re in get_all_colleges_link:
    ReviewDetails(re)


# In[32]:


#cutoff 

def CutOffDetails(url):
    
    page=requests.get(url+"/cutoff")
    if page.status_code == 200:
            soup = BeautifulSoup(page.text,'html.parser')
            rows=soup.find_all("table", class_=" table table-striped style_table")
            if rows is None:
                rows=soup.find_all("table", class_="table table-striped dates_table")
                for row in rows:
                    cutoff.append(row.get_text())
                    thewriter.writerow({'Cut oFF':row.get_text()})
            else:
                for row in rows:
                    cutoff.append(row.get_text())
                    thewriter.writerow({'Cut oFF':row.get_text()})


# In[33]:


for cutoff in get_all_colleges_link:
    CutOffDetails(cutoff)


# In[34]:


f.close()


# In[ ]:




