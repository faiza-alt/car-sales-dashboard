import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('vehicles_us.csv')

# App title
st.title('Car Sales Dashboard')

# Header
st.header('Price Distribution')

# Plot histogram
fig = px.histogram(df, x='price')
st.plotly_chart(fig)

# Header
st.header('Price vs Year')

# Plot scatter plot
fig = px.scatter(df, x='year', y='price', color='model')
st.plotly_chart(fig)

# Checkbox to show/hide raw data
if st.checkbox('Show raw data'):
    st.write(df)