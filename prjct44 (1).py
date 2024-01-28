#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import plotly.express as px
import altair as alt
import plotly.graph_objects as go
import matplotlib.pyplot as plt



# In[2]:


file_path = r'C:\Users\hp\Downloads\vehicles_us (1).csv'

# Read the CSV file into a Pandas DataFrame
vehicles_df = pd.read_csv(file_path)

# Display basic information about the DataFrame
print(vehicles_df.info())

# Explore the first few rows of the DataFrame
print(vehicles_df.head())


# In[3]:


vehicles_df


# In[4]:


vehicles_df.head()


# In[5]:


vehicles_df.describe()


# In[6]:


# Check for duplicated 
vehicles_df.duplicated().sum()


# In[7]:


vehicles_df.dtypes


# In[8]:


display("\nCategorical Features:")
for column in vehicles_df.select_dtypes(include='object').columns:
    display(f"\n{column}:\n{vehicles_df[column].value_counts()}")


# In[9]:


plt.scatter(vehicles_df['odometer'], vehicles_df['price'], alpha=0.5)
plt.xlabel('Odometer (miles)')
plt.ylabel('Price ($)')
plt.title('Scatter Plot: Price vs Odometer')
plt.grid(True)
plt.show()


# In[10]:


vehicles_df['odometer_range'] = pd.cut(vehicles_df['odometer'], bins=10)

# Convert 'odometer_range' to string for plotting
vehicles_df['odometer_range_str'] = vehicles_df['odometer_range'].astype(str)

# Calculate the average price for each odometer range
average_price_by_odometer = vehicles_df.groupby('odometer_range_str')['price'].mean().reset_index()

# Create a bar chart
plt.figure(figsize=(12, 6))
plt.bar(average_price_by_odometer['odometer_range_str'], average_price_by_odometer['price'], alpha=0.7)
plt.xlabel('Odometer Range (miles)')
plt.ylabel('Average Price ($)')
plt.title('Average Price vs Odometer Range')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# In[ ]:





# In[ ]:




