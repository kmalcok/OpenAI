import streamlit as st
import entity as e
import pandas as pd

# Load DataFrame
df = e.df

# Streamlit App
st.title("Sales by Category and Date")

# Selectbox for category selection
categories = df['Category'].unique()
selected_category = st.selectbox("Select Category", categories)

# Filter data based on selected category
filtered_df = df[df['Category'] == selected_category]

# Grouping sales data by Date
sales_by_date = filtered_df.groupby('Date')['Sales'].sum().reset_index()

# Display bar chart
st.bar_chart(sales_by_date.set_index('Date'))