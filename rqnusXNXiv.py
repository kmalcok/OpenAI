import streamlit as st
import entity as e

# Load data
df = e.df

# Group data by 'Category' and sum the 'Sales'
category_sales = df.groupby('Category')['Sales'].sum().reset_index()

# Display bar chart
st.bar_chart(category_sales.set_index('Category'))