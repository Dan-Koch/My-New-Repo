#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing any libraries we may need
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import requests
import json
import plotly_express as px
import streamlit as st


# In[2]:


#importing dataframe
vehicles_us = pd.read_csv('/Users/danie/My-New-Repo/vehicles_us.csv')


# In[3]:


#creating a header with streamlit
st.header('Information on Cars in the US')


# In[4]:


#creating a selectbox
model_veh = vehicles_us['model'].unique()
vehicle_select = st.selectbox('model:', model_veh)


# In[5]:


#creating a slider for the model year
#variables for the min and max of the slider
min_year= int(vehicles_us['model_year'].min())
max_year= int(vehicles_us['model_year'].max())

#creating a slider
year_range = st.slider("Choose years", value= (min_year, max_year), min_value= min_year, max_value= max_year)
real_range = list(range(year_range[0], year_range[1]+ 1))


# In[6]:


#filtering dataframe based on selectbox and year range
filter_model_year = vehicles_us[(vehicles_us['model'] == vehicle_select) & (vehicles_us['model_year'].isin(list(real_range)))]

#showing the information the user selected
st.table(filter_model_year)


# In[7]:


#creating a list for historgram
list_for_hist= ['odometer', 'fuel', 'type', 'condition',]

#creating a selectbox for histogram
hist_select= st.selectbox('Choose for price distribution', list_for_hist)

#histogram with price as the x axis and user chooses the y axis
graph1= px.histogram(vehicles_us, x='price', color= hist_select)

#adding title
graph1.update_layout(title= "<b>Split of Price by{}</b>".format(hist_select))

st.plotly_chart(graph1)


# In[9]:


#creating a scatter plot of price vs a one column from a list
#creating a list to choose from
list_for_scatter = ['odometer', 'days_listed', 'cylinders']

#creating a selectbox for scatterplot
scatter_select= st.selectbox('Price dependency on ', list_for_scatter)
graph2= px.scatter(vehicles_us, x= 'price', y= scatter_select, hover_data=['model_year'])

#adding title
graph2.update_layout(title="<b>Price vs {}</b>".format(scatter_select))
st.plotly_chart(graph2)


# In[ ]:



