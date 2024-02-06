#!/usr/bin/env python
# coding: utf-8

# Q1. What are the three measures of central tendency?

# There are three main measures of central tendency:
#     1. Mean
#     2. Meadian
#     3. Mode
# 
# 1. Mean : It is also known as avrage. The mean is the sum of the value of each observation in a dataset divided by the number of observations.
# 2. Meadian : The median is the middle value in distribution when the values are arranged in ascending or descending order.
# 3. Mode : The mode is the most commonly occurring value in a distribution.

# Q2. What is the difference between the mean, median, and mode? How are they used to measure the
# central tendency of a dataset?

# In[3]:


import numpy as np


# In[4]:


x = [1,2,3,4,5]


# In[5]:


len(x)


# In[8]:


np.mean(x)


# There are 2 cases in median like even and odd

# even case 

# In[9]:


even = [1,2,3,4,5,6]


# In[10]:


len(even)


# In[11]:


np.median(even)


# odd case

# In[12]:


odd = [1,2,3,4,5]


# In[13]:


np.median(odd)


# Mode

# In[31]:


from scipy import stats

rank = [ 3, 3, 6, 9, 15, 15, 15, 27, 27, 37, 48]


# In[32]:


stats.mode(rank)


# Q3. Measure the three measures of central tendency for the given height data:
# [178,177,176,177,178.2,178,175,179,180,175,178.9,176.2,177,172.5,178,176.5]

# In[33]:


x = [178,177,176,177,178.2,178,175,179,180,175,178.9,176.2,177,172.5,178,176.5]


# Mean

# In[34]:


import numpy as np


# In[35]:


np.mean(x)


# In[36]:


np.median(x)


# In[37]:


from scipy import stats


# In[38]:


stats.mode(x)


# Q4. Find the standard deviation for the given data:
# [178,177,176,177,178.2,178,175,179,180,175,178.9,176.2,177,172.5,178,176.5]

# In[39]:


x = [178,177,176,177,178.2,178,175,179,180,175,178.9,176.2,177,172.5,178,176.5]


# In[40]:


import statistics


# In[41]:


statistics.stdev(x)


# Q7. For the two given sets A = (2,3,4,5,6,7) & B = (0,2,6,8,10). Find:
# (i) A B
# (ii) A ⋃ B

# In[44]:


A = {2,3,4,5,6,7}
B = {0,2,6,8,10}


# A U B

# In[45]:


print("A U B:", A.union(B))


# In[46]:


print("A B:", A.intersection(B))


# In[ ]:





# Q8. What do you understand about skewness in data?

# Skewness is a measure of the asymmetry of a distribution. A distribution is asymmetrical when its left and right side are not mirror images.
# 
# A distribution can have right (or positive), left (or negative), or zero skewness. A right-skewed distribution is longer on the right side of its peak, and a left-skewed distribution is longer on the left side of its peak:

# Q11. What is the formula for calculating the sample mean? Provide an example calculation for a
# dataset.

# The sample mean formula is used to calculate the average value of the given sample data.
# Sample Mean = (Sum of terms) ÷ (Number of Terms)
# Sample Mean = x1+x2+x3+....+/n
# 
# sample mean = 1+2+3+4+5/5 = 3

# Q6. What is a Venn diagram?

# A Venn diagram uses overlapping circles or other shapes to illustrate the logical relationships between two or more sets of items.
# 

# In[54]:


get_ipython().system('pip install matplotlib-venn')


# In[60]:


from matplotlib_venn import venn2  
from matplotlib import pyplot as plt 
  
# depict venn diagram 
venn2(subsets = (40, 40, 20), set_labels = ('Sec A', 'Sec B')) 
plt.show()


# Q14. How do outliers affect measures of central tendency and dispersion? Provide an example.

# Measures of Central Tendency:
# 
#     Mean: Outliers can pull the mean towards their extreme values. If there are outliers with large values, the mean can be inflated, while outliers with small values can lower the mean.
#     Median: The median is less affected by outliers compared to the mean. It represents the middle value, so outliers have less impact unless they are close to the median and significantly change the order of values.
#     Mode: The mode is the most frequent value. Outliers do not directly affect the mode unless they appear frequently and change the overall distribution of values.
# 
# Measures of Dispersion:
# 
#     Range: The range is the difference between the maximum and minimum values. Outliers can significantly increase the range if they are far from the other values.
#     Interquartile Range (IQR): The IQR is less affected by outliers compared to the range since it only considers the values within the 25th and 75th percentiles. However, extreme outliers can still impact the IQR.
#     Standard Deviation/Variance: Outliers can increase the standard deviation and variance, as they introduce more variability to the dataset. The squared differences between outliers and the mean can significantly contribute to the variance.
# 

# Q13. How is covariance different from correlation?

# Covariance :Covariance is an indicator of the extent to which 2 random variables are dependent on each other. A higher number denotes higher dependency.The value of covariance lies in the range of -∞ and +∞.Affects covariance
# 
# Correlation :Correlation is a statistical measure that indicates how strongly two variables are related.Correlation is limited to values between the range -1 and +1.Does not affect the correlation    

# In[ ]:




