#!/usr/bin/env python
# coding: utf-8

# In[18]:


import streamlit as st
import plotly.express as px
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline


# In[19]:


dataset=pd.read_excel('owid_covid_latest_cleaned.xlsx')


# In[20]:


st.set_page_config(page_title="InfecTech", page_icon=":microbe:", layout="wide")
st.markdown("<h1 style='text-align: center; font-size: 78px;  margin-top: -75px; font-family: Georgia, serif; color: LimeGreen;'>InfecTech</h1>", unsafe_allow_html=True)


# In[2]:


df2 = pd.read_csv('owid_covid_latest_cleaned.csv')


# In[3]:


st.write("This graph is performing a type of data analysis called clustering on a dataset of population and COVID-19 total cases. The output gives an idea of how the countries are grouped based on their population and total number of COVID-19 cases.")


# In[6]:


import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import plotly.express as px
import streamlit as st

# Select the columns of interest from the dataframe
data = df2[['population', 'total_cases']]

# Drop any rows with missing values
data = data.dropna(subset=['population', 'total_cases'])

# Standardize the data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data[['total_cases']])

# Determine the optimal number of clusters using the elbow method
elbow_scores = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=0).fit(data_scaled)
    elbow_scores.append(kmeans.inertia_)

# Create a DataFrame to hold the elbow scores
elbow_df = pd.DataFrame({'k': range(2, 11), 'inertia': elbow_scores})

# Plot the elbow curve
fig = px.line(elbow_df, x='k', y='inertia', title='Elbow Curve')
st.plotly_chart(fig)

st.write("The cluster graph shows insights into how the data points are grouped and distributed among different clusters. The plot allows you to observe patterns, similarities, or differences in the distribution of total_cases values across different population levels.")
# Perform K-means clustering with the optimal number of clusters
k = 3  # Specify the number of clusters based on the elbow curve
kmeans = KMeans(n_clusters=k, random_state=0).fit(data_scaled)

# Add the cluster labels to the original DataFrame
data['Cluster'] = kmeans.labels_

# Print the mean total_cases for each cluster
cluster_means = data.groupby(['Cluster'])['total_cases'].mean()
print(cluster_means)

# Plot the cluster graph
fig_cluster = px.scatter(data, x='population', y='total_cases', color='Cluster', title='Cluster Graph')
st.plotly_chart(fig_cluster)


# In[24]:


st.header("Predictions")


# In[25]:


size = st.number_input("Enter a population size to predict cases: ")


# In[37]:


d1 = df2[['population', 'total_cases']]
d1 = d1.dropna(subset=['population', 'total_cases'])

Xtrain, x_test, Ytest, Y_test = train_test_split(d1[['population']], d1['total_cases'], test_size=0.2, random_state=0)

scaler1 = StandardScaler()
Xtrain_scaled = scaler1.fit_transform(Xtrain)
x_test_scaled = scaler1.transform(x_test)

# train a linear regression1ression model
regression1 = LinearRegression().fit(Xtrain_scaled, Ytest)

# make predictions on new d1
new_d1 = pd.DataFrame({'population': [size]})
new_d1_scaled = scaler1.transform(new_d1)
predictions1 = regression1.predict(new_d1_scaled)

# print the predictions
print(predictions1)


# In[38]:


st.write(f"According to the population size you entered, the predicted total cases are {predictions1}")


# In[28]:


size1 = st.number_input("Enter a population size to predict deaths: ")


# In[39]:


d2 = df2[['population', 'total_deaths']]

# drop any rows with missing values
d2 = d2.dropna(subset=['population', 'total_deaths'])

# split the data into training and testing sets
Xtrain1, x_test1, Ytrain1, y_test1 = train_test_split(d2[['population']], d2['total_deaths'], test_size=0.2, random_state=0)

# standardize the data
scaler2 = StandardScaler()
Xtrain1_scaled = scaler2.fit_transform(Xtrain1)
x_test1_scaled = scaler2.transform(x_test1)

# train a linear regression model
regression2 = LinearRegression().fit(Xtrain1_scaled, Ytrain1)

# make predictions on new data
new_d2 = pd.DataFrame({'population': [size1]})
new_d2_scaled = scaler2.transform(new_d2)
predictions2 = regression2.predict(new_d2_scaled)

# print the predictions
print(predictions2)


# In[43]:


st.write(f"According to the population size you entered, the predicted total deaths are {predictions2}")


# In[41]:


hide = """
         <style>
         footer {visibility:hidden;}
         </style>
         """


# In[42]:


st.markdown(hide, unsafe_allow_html = True)


# In[ ]:




