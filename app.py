#!/usr/bin/env python
# coding: utf-8

# In[167]:


import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image


# In[168]:


dataset=pd.read_excel('owid_covid_latest_cleaned.xlsx')


# In[176]:


st.set_page_config(page_title="InfecTech", page_icon=":microbe:", layout="wide")


# In[187]:


st.markdown("<h1 style='text-align: center; font-size: 78px;  margin-top: -75px; font-family: Georgia, serif; color: LimeGreen;'>InfecTech</h1>", unsafe_allow_html=True)


# In[181]:


st.sidebar.image('covvv.png', use_column_width = False, width=50)


# In[179]:


st.sidebar.header("Browse")


# In[180]:


location=st.sidebar.multiselect("Filter By Location: ",
                               options=dataset["location"].unique(),
#                                default=dataset["location"].unique()
)


# In[134]:


selection_query=dataset.query("location==@location")


# In[135]:


#st.dataframe(selection_query)


# In[137]:


totalcases=(selection_query["total_cases"].sum())
totaldeaths=(selection_query["total_deaths"].sum())


# In[138]:


first_column, second_column = st.columns(2)


# In[139]:


with first_column:
    st.markdown("### Total Cases:")
    st.subheader(f'{totalcases} ')
with second_column:
    st.markdown("### Total Deaths:")
    st.subheader(f'{totaldeaths} ')


# In[140]:


st.markdown("---")


# In[141]:


cases_by_loc = selection_query.groupby(by=["location"]).sum()[["total_cases"]]


# In[142]:


cbl_barchart = px.bar(cases_by_loc,
                      x = "total_cases",
                      y = cases_by_loc.index, title = "Cases by Location",
                      color_discrete_sequence = ["DodgerBlue"])


# In[143]:


cbl_barchart.update_layout(plot_bgcolor = "rgba(0,0,0,0)",
                    xaxis = (dict(showgrid = False)))


# In[144]:


print(cases_by_loc)


# In[145]:


deaths_by_loc = selection_query.groupby(by=["location"]).sum()[["total_deaths"]]


# In[146]:


dbl_barchart = px.bar(deaths_by_loc,
                      x = "total_deaths",
                      y = deaths_by_loc.index, title = "Deaths by Location",
                      color_discrete_sequence = ["FireBrick"])


# In[147]:


dbl_barchart.update_layout(plot_bgcolor = "rgba(0,0,0,0)",
                    xaxis = (dict(showgrid = False)))


# In[148]:


print(deaths_by_loc)


# In[149]:


left_column, right_column = st.columns(2)


# In[150]:


left_column.plotly_chart(cbl_barchart, use_container_width = True)


# In[151]:


right_column.plotly_chart(dbl_barchart, use_container_width = True)


# In[152]:


hide = """
         <style>
         footer {visibility:hidden;}
         </style>
         """


# In[153]:


st.markdown(hide, unsafe_allow_html = True)


# In[182]:


st.dataframe(selection_query)


# In[154]:


visualisation = st.sidebar.selectbox('Select a Chart Type', ('Pie Chart', 'Line Chart'))
#country_select = st.sidebar.selectbox('Select a Country', dataset['location'].unique())
status_select = st.sidebar.radio("Covid-19 Case Status", ('total_cases', 'total_deaths', 'new_cases'))
#selected_country = dataset[dataset['location']==country_select]
st.markdown('# Country Level Analysis')


# In[155]:


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
    else:
        st.header("Total Death Cases ")
        fig = px.pie(dataset, values=dataset['total_deaths'], names=dataset['location'])
        st.plotly_chart (fig)
elif visualisation=='Line Chart':
    if status_select == 'total_cases':
        st.header("Total Confirmed Cases Among Countries")
        fig = px.line(dataset, x=dataset['location'], y=dataset['total_cases'])
        st.plotly_chart(fig)
    elif status_select=='newcases':
        st.header("Total Active Cases Among Countries")
        fig = px.line(dataset, x=dataset['location'], y=dataset['new_cases'])
        st.plotly_chart(fig)
    else:
        st.header("Total Deaths Among Countries")
        fig = px.line(dataset, x=dataset['location'], y=dataset['total_deaths'])
        st.plotly_chart(fig)


# In[ ]:





# In[ ]:




