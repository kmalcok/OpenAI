import streamlit as st
import entity as e
import pandas as pd

# Function to refresh the data
def refresh_data():
    st.experimental_rerun()

# Streamlit UI
st.title("Sales by Category and Weekday")

# Add a refresh button
if st.button("Refresh Data"):
    refresh_data()

# Load data from entity module
df = e.df

# Ensure Date column is in datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Group data by Category and sum Sales
category_sales = df.groupby("Category")["Sales"].sum()

# Group data by Weekday and sum Sales
weekday_sales = df.groupby("Weekday")["Sales"].sum()

# Display category sales chart
st.subheader("Sales by Category")
st.bar_chart(category_sales)

# Display weekday sales chart
st.subheader("Sales by Weekday")
st.bar_chart(weekday_sales)