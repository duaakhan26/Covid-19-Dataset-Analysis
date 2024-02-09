#!/usr/bin/env python
# coding: utf-8

# In[12]:


import streamlit as st
import plotly.express as px
import pandas as pd


# In[13]:


dataset=pd.read_excel('owid_covid_latest_cleaned.xlsx')


# In[14]:


st.set_page_config(page_title="InfecTech", page_icon=":microbe:", layout="wide")
st.markdown("<h1 style='text-align: center; font-size: 78px;  margin-top: -75px; font-family: Georgia, serif; color: LimeGreen;'>InfecTech</h1>", unsafe_allow_html=True)


# In[15]:


st.sidebar.header("Browse")


# In[16]:


visualisation = st.sidebar.selectbox('Select a Chart Type', ('Pie Chart', 'Line Chart'))
#country_select = st.sidebar.selectbox('Select a Country', dataset['location'].unique())
status_select = st.sidebar.radio("Covid-19 Case Status", ('population', 'total_cases', 'total_deaths', 'new_cases', 'total_vaccinations', 'total_boosters', 'handwashing_facilities', 'cardiovasc_death_rate'))
#selected_country = dataset[dataset['location']==country_select]
st.markdown("<h1 style='text-align: center; font-size: 50px; '>Country Level Analysis</h1>", unsafe_allow_html=True)


# In[17]:


def get_total_dataframe(dataset):
    total_dataframe = pd.DataFrame({
        'Status': ['New', 'Deaths', 'Confirmed'],
        'Number of cases': [dataset.iloc[0]['new_cases'], dataset.iloc[0]['total_deaths'], dataset.iloc[0]['total_cases']]
    })
    return total_dataframe

#state_total = get_total_dataframe(selected_country)
if visualisation=='Pie Chart':
    if status_select== 'total_cases':
        st.header("Total Confirmed Cases ")
        fig = px.pie(dataset, values=dataset['total_cases'], names=dataset['location'])
        st.plotly_chart (fig)
    elif status_select=='new_cases':
        st.header("Total Active Cases ")
        fig = px.pie(dataset, values=dataset['new_cases'], names=dataset['location'])
        st.plotly_chart (fig)
    elif status_select=='total_deaths':
        st.header("Total Death Cases ")
        fig = px.pie(dataset, values=dataset['total_deaths'], names=dataset['location'])
        st.plotly_chart (fig)
    elif status_select=='total_vaccinations':
        st.header("Total Vaccinations ")
        fig = px.pie(dataset, values=dataset['total_vaccinations'], names=dataset['location'])
        st.plotly_chart (fig)
    elif status_select=='total_boosters':
        st.header("Total Boosters ")
        fig = px.pie(dataset, values=dataset['total_boosters'], names=dataset['location'])
        st.plotly_chart (fig)
    elif status_select=='handwashing_facilities':
        st.header("Handwashing Facilities ")
        fig = px.pie(dataset, values=dataset['handwashing_facilities'], names=dataset['location'])
        st.plotly_chart (fig)
    elif status_select=='population':
        st.header("Population ")
        fig = px.pie(dataset, values=dataset['population'], names=dataset['location'])
        st.plotly_chart (fig)
    elif status_select=='cardiovasc_death_rate':
        st.header("Cardiovascular Death Rate ")
        fig = px.pie(dataset, values=dataset['cardiovasc_death_rate'], names=dataset['location'])
        st.plotly_chart (fig)
elif visualisation=='Line Chart':
    if status_select == 'total_cases':
        st.header("Total Confirmed Cases Among Countries")
        fig = px.line(dataset, x=dataset['location'], y=dataset['total_cases'])
        st.plotly_chart(fig)
    elif status_select=='new_cases':
        st.header("Total Active Cases Among Countries")
        fig = px.line(dataset, x=dataset['location'], y=dataset['new_cases'])
        st.plotly_chart(fig)
    elif status_select=='total_deaths':
        st.header("Total Deaths Among Countries")
        fig = px.line(dataset, x=dataset['location'], y=dataset['total_deaths'])
        st.plotly_chart(fig)
    elif status_select=='total_vaccinations':
        st.header("Total Vaccinations Among Countries")
        fig = px.line(dataset, x=dataset['location'], y=dataset['total_vaccinations'])
        st.plotly_chart(fig)
    elif status_select=='total_boosters':
        st.header("Total Boosters Among Countries")
        fig = px.line(dataset, x=dataset['location'], y=dataset['total_boosters'])
        st.plotly_chart(fig)
    elif status_select=='handwashing_facilities':
        st.header("Handwashing Facilities Among Countries")
        fig = px.line(dataset, x=dataset['location'], y=dataset['handwashing_facilities'])
        st.plotly_chart(fig)
    elif status_select=='population':
        st.header("Population Among Countries")
        fig = px.line(dataset, x=dataset['location'], y=dataset['population'])
        st.plotly_chart(fig)
    elif status_select=='cardiovasc_death_rate':
        st.header("Cardiovascular Death Rate Among Countries")
        fig = px.line(dataset, x=dataset['location'], y=dataset['cardiovasc_death_rate'])
        st.plotly_chart(fig)


# In[18]:


hide = """
         <style>
         footer {visibility:hidden;}
         </style>
         """


# In[19]:


st.markdown(hide, unsafe_allow_html = True)


# In[ ]:




