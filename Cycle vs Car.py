#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import math
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[10]:


df = pd.read_excel(r"C:\Users\User\Desktop\cycle\pagol.xlsx")


print(df.columns)
df.head()


# In[7]:


df.drop(["Unnamed: 0",'Less than 1', '1–5','\n6–10', '\nMore than 10 '
         ,'Like bicycling', 'Unnamed: 18' ], axis=1, inplace=True)
df.head()


# In[8]:


df.describe()


# In[9]:


from scipy.stats import shapiro
stat, p = shapiro(df["BMI"])
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
    print('Probably Gaussian')
else:
    print('Probably not Gaussian')


# In[10]:


sns.displot(df['BMI'])


# In[11]:


print(df.columns)


# In[12]:


ax = sns.countplot(x="Vehicle Type",
                   hue="Obesity Related Disease",
                   data = df)
plt.show()


# In[13]:


ax = sns.p(x="Vehicle Type",
                   hue="Bmi cateogry",
                   data = df)


# In[14]:


sns.displot(df, x="BMI", hue="Vehicle Type", element="step")


# In[15]:





# In[30]:


df.groupby(by="Vehicle Type").mean()


# In[20]:


df.groupby(by="Vehicle Type").max()


# In[21]:


df.groupby(by="Vehicle Type").min()


# In[23]:


from scipy.stats import chi2_contingency


contigency= pd.crosstab(df['Vehicle Type'], df['Obesity Related Disease'])
contigency


# In[24]:


''' Ho: "Vehicle Type" and "Obesity Related Disease" are Independent
    H1: "Vehicle Type" and "Obesity Related Disease" are Dependent
'''

c, p, dof, expected = chi2_contingency(contigency)

print("p_value: ",round(p,3))


# In[26]:


'''
0.008 < 0.5
reject null Hypothesis
so Vehicle Type" and "Obesity Related Disease" are Dependent
'''


# In[27]:


contigency= pd.crosstab(df['Vehicle Type'], df['Daily Commute Distance '])
contigency


# In[28]:


c, p, dof, expected = chi2_contingency(contigency)

print("p_value: ",round(p,3))


# In[29]:


'''
0.824 > 0.5
Accept null Hypothesis
so Vehicle Type" and "Daily Commute Distance " are Independent
'''


# In[31]:





# In[35]:


contigency= pd.crosstab(df['Vehicle Type'], df['Bmi cateogry'])
contigency


# In[36]:


c, p, dof, expected = chi2_contingency(contigency)

print("p_value: ",round(p,3))


# In[44]:


'''
0.0 < 0.5
reject null Hypothesis
so Vehicle Type" and "Bmi cateogry" are Dependent
'''
df.rename(columns={"Vehicle Type": "Vehicle"}, inplace=True)


# In[47]:


from scipy.stats import ttest_ind

'''
    Sample Question: Is there a difference in "AGE" between "CAR USER" and "BICYCLE USER"?
    Ho: There is no difference
    H1: There is a difference
'''

t_stat, p = ttest_ind(df.query('Vehicle=="Car"')['Age'], df.query('Vehicle=="Bicycle"')['Age'])

print("p_value: ",round(p,3))


# In[46]:


df.head(30)


# In[49]:


sns.displot(df, x="Age", hue="Vehicle", element="step")


# In[60]:


car_ownr = df.loc[df["Vehicle"] == 'Car']
car_ownr.columns
car_ownr.dropna(inplace=True)
len(car_ownr)


# In[70]:


df.columns


# In[97]:


df.rename(columns={"Disease?": "Disease",
                   "Switch?": "Switch",
                   "Aware?": "Aware",
                   "Distance?": "Distance",
                   "Cost incurred" : "CostIncurred"}, inplace=True)
df.columns


# In[163]:


car_pagla = pagla.loc[pagla["Vehicle"] == 0]
pagla.head()
pagla.rename(columns={"switch " : "switch"}, inplace=True)
pagla.columns


# In[166]:


reg3 = ols("BMI ~  Disease + Vehicle", data = pagla).fit(cov_type = 'HC3')
print(reg3.summary())


# In[151]:



car_pagla.rename(columns={"switch ": "switch"}, inplace=True)


# In[152]:


car_pagla.columns

