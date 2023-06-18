#!/usr/bin/env python
# coding: utf-8

#importing any libraries we may need
import pandas as pd
import plotly_express as px
import streamlit as st

#importing dataframe
vehicles_us = pd.read_csv('vehicles_us.csv')

#filling paint color with unknown
vehicles_us['paint_color'].fillna('unknown', inplace= True)

#filling model_year NaN values with median after grouping by model
vehicles_us['model_year']= vehicles_us['model_year'].fillna(vehicles_us.groupby('model')['model_year'].transform('median'))

#filling cylinder NaN values with median after grouping by model
vehicles_us['cylinders']= vehicles_us['cylinders'].fillna(vehicles_us.groupby('model')['cylinders'].transform('median'))

#filling odometer NaN values with median after grouping by model_year
#i am grouping by year, because in theory the older the vehicle the higher the odometer value
vehicles_us['odometer']= vehicles_us['odometer'].fillna(vehicles_us.groupby('model_year')['cylinders'].transform('median'))

#filling NaN values with 0 for is_4wd
vehicles_us['is_4wd'].fillna(0, inplace= True)

#creating a header with streamlit
st.header('Information on Cars in the US')
st.dataframe(vehicles_us)

#creating a list for historgram
list_for_hist= ['odometer', 'fuel', 'type', 'condition',]

#creating a selectbox for histogram
hist_select= st.selectbox('Choose for price distribution', list_for_hist, index= 0)

#histogram with price as the x axis and user chooses the y axis
graph1= px.histogram(vehicles_us, x='price', color= hist_select)

#adding title
graph1.update_layout(title= "<b>Split of Price by {}</b>".format(hist_select))

st.plotly_chart(graph1)

#creating a scatter plot of price vs a one column from a list
#creating a list to choose from
list_for_scatter = ['odometer', 'days_listed', 'cylinders', 'condition']

#creating a selectbox for scatterplot
scatter_select= st.selectbox('Price dependency on ', list_for_scatter, index= 0)
graph2= px.scatter(vehicles_us, x= 'price', y= scatter_select, hover_data=['model_year'])

#adding title
graph2.update_layout(title="<b>Price vs {}</b> ".format(scatter_select))
st.plotly_chart(graph2)

#creatting a scatter plot of days listed vs a few columns from a list
list_for_hist_days= ['price', 'condition', 'transmission', 'fuel', 'model_year']
hist_select_days= st.selectbox('Select a column to see how many days it is listed', list_for_hist_days, index= 0)

graph3= px.histogram(vehicles_us, x= 'days_listed', y= hist_select_days, color= hist_select_days)
graph3.update_layout(title= "<b> Days listed vs {}</b>".format(hist_select_days))
st.plotly_chart(graph3)

#creating a checkbox to show a correlation matrix when true
corr_matrix_checkbox = st.checkbox('Display Correlation Matrix?')
corr_vehicles = vehicles_us[['price','model_year', 'cylinders', 'odometer','days_listed']]
corr_matrix = corr_vehicles.corr()

if corr_matrix_checkbox:
    st.dataframe(corr_matrix)
