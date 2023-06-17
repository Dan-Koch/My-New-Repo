#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing any libraries we may need
import pandas as pd
import plotly_express as px
import streamlit as st


# In[2]:
#importing dataframe
vehicles_us = pd.read_csv('/Users/danie/My-New-Repo/vehicles_us.csv')

#filling paint color with unknown
vehicles_us['paint_color'].fillna('unknown', inplace= True)

#filling median year in for NaN values
year_median = vehicles_us['model_year'].median()
vehicles_us['model_year'].fillna(year_median, inplace= True)

#filling median cylinders in for NaN values
cylinder_median = vehicles_us['cylinders'].median()
vehicles_us['cylinders'].fillna(cylinder_median, inplace= True)

#filling median odometer reading into NaN values
odometer_median = vehicles_us['odometer'].median()
vehicles_us['odometer'].fillna(odometer_median, inplace= True)

#filling NaN values with 0 for is_4wd
vehicles_us['is_4wd'].fillna(0, inplace= True)
# In[3]:
#creating a header with streamlit
st.header('Information on Cars in the US')
st.dataframe(vehicles_us)

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
st.write("Here you see all the vehicles of the model you selected that was built within the years on the slider.")
st.table(filter_model_year)


# In[7]:
#creating a list for historgram
list_for_hist= ['odometer', 'fuel', 'type', 'condition',]

#creating a selectbox for histogram
hist_select= st.selectbox('Choose for price distribution', list_for_hist)

#histogram with price as the x axis and user chooses the y axis
graph1= px.histogram(vehicles_us, x='price', color= hist_select)

#adding title
graph1.update_layout(title= "<b>Split of Price by {}</b>".format(hist_select))

st.plotly_chart(graph1)


# In[9]:
#creating a scatter plot of price vs a one column from a list
#creating a list to choose from
list_for_scatter = ['odometer', 'days_listed', 'cylinders', 'condition']

#creating a selectbox for scatterplot
scatter_select= st.selectbox('Price dependency on ', list_for_scatter)
graph2= px.scatter(vehicles_us, x= 'price', y= scatter_select, hover_data=['model_year'])

#adding title
graph2.update_layout(title="<b>Price vs {}</b> ".format(scatter_select))
st.plotly_chart(graph2)


# In[ ]:
# #creatting a scatter plot of days listed vs a few columns from a list
list_for_hist_days= ['price', 'condition', 'transmission', 'fuel', 'model_year']
hist_select_days= st.selectbox('Select a column to see how many days it is listed', list_for_hist_days)

graph3= px.histogram(vehicles_us, x= 'days_listed', y= hist_select_days, color= hist_select_days)
graph3.update_layout(title= "<b> Days listed vs {}</b>".format(hist_select_days))
st.plotly_chart(graph3)

#creating a checkbox to show a correlation matrix when true
corr_matrix_checkbox = st.checkbox('Display Correlation Matrix?')
corr_vehicles = vehicles_us[['price','model_year', 'cylinders', 'odometer','days_listed']]
corr_matrix = corr_vehicles.corr()

if corr_matrix_checkbox:
    st.dataframe(corr_matrix)
