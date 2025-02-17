import streamlit as st
import entity as e

# Load data
df = e.df

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Group by Date and sum Sales
daily_sales = df.groupby('Date')['Sales'].sum().reset_index()

# Group by Category and sum Sales
category_sales = df.groupby('Category')['Sales'].sum().reset_index()

# Streamlit app
st.title("Sales Analysis")

# Daily Sales Visualization
st.subheader("Gün Bazında Satışlar")
st.bar_chart(daily_sales.set_index('Date'))

# Category Sales Visualization
st.subheader("Kategori Bazında Satışlar")
st.bar_chart(category_sales.set_index('Category'))