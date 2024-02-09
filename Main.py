#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image


# In[2]:


dataset=pd.read_excel('owid_covid_latest_cleaned.xlsx')


# In[3]:


import toml


# In[4]:


st.set_page_config(page_title="InfecTech", page_icon=":microbe:", layout="wide")


# In[5]:


st.markdown("<h1 style='text-align: center; font-size: 78px;  margin-top: -75px; font-family: Georgia, serif; color: LimeGreen;'>InfecTech</h1>", unsafe_allow_html=True)


# In[6]:


st.sidebar.image('covvv.png', use_column_width = False, width=75)


# In[7]:


st.sidebar.header("Browse")


# In[28]:


location=st.sidebar.multiselect("Filter By Location: ",
                               options=dataset["location"].unique(),
#                                default=dataset["location"].unique()
)


# In[9]:


selection_query=dataset.query("location==@location")


# In[10]:


totalcases=(selection_query["total_cases"].sum())
totaldeaths=(selection_query["total_deaths"].sum())


# In[11]:


first_column, second_column = st.columns(2)


# In[12]:


with first_column:
    st.markdown("### Total Cases:")
    st.subheader(f'{totalcases} ')
with second_column:
    st.markdown("### Total Deaths:")
    st.subheader(f'{totaldeaths} ')


# In[13]:


st.markdown("---")


# In[14]:


cases_by_loc = selection_query.groupby(by=["location"]).sum()[["total_cases"]]


# In[15]:


cbl_barchart = px.bar(cases_by_loc,
                      x = "total_cases",
                      y = cases_by_loc.index, title = "Cases by Location",
                      color_discrete_sequence = ["#e39ff6"])


# In[16]:


cbl_barchart.update_layout(plot_bgcolor = "rgba(0,0,0,0)",
                    xaxis = (dict(showgrid = False)))


# In[17]:


print(cases_by_loc)


# In[18]:


deaths_by_loc = selection_query.groupby(by=["location"]).sum()[["total_deaths"]]


# In[19]:


dbl_barchart = px.bar(deaths_by_loc,
                      x = "total_deaths",
                      y = deaths_by_loc.index, title = "Deaths by Location",
                      color_discrete_sequence = ["FireBrick"])


# In[20]:


dbl_barchart.update_layout(plot_bgcolor = "rgba(0,0,0,0)",
                    xaxis = (dict(showgrid = False)))


# In[21]:


print(deaths_by_loc)


# In[22]:


left_column, right_column = st.columns(2)


# In[23]:


left_column.plotly_chart(cbl_barchart, use_container_width = True)


# In[24]:


right_column.plotly_chart(dbl_barchart, use_container_width = True)


# In[25]:


hide = """
         <style>
         footer {visibility:hidden;}
         </style>
         """


# In[26]:


st.markdown(hide, unsafe_allow_html = True)


# In[27]:


st.dataframe(selection_query)


# In[ ]:





# In[ ]:




