# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 01:06:55 2025

@author: ACER
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')
url='https://raw.githubusercontent.com/Hoshino1ka/Hoshi/refs/heads/main/hour.csv'
hour=pd.read_csv(url)
datetime_columns = ['dteday']

st.header('Bike Rental Dashboard :sparkles:')

st.subheader("Highest Rental Based on Season and workday or not.")

plot_type = st.radio("Select plot type:", ("Season", "Workday"))

# Plot based on selection
fig, ax = plt.subplots()
if plot_type == "Season":
    plt.figure(figsize=(10, 5))
    colors = ["#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3"]
    data1 = hour.groupby(by='season').cnt.mean().sort_values(ascending=False).reset_index()
    sns.barplot(
        y="cnt",
        x="season",
        data=data1,
        palette=colors
    )
    plt.title("Number of Rental", loc="center", fontsize=15)
    plt.ylabel(None)
    plt.xlabel(None)
    plt.xticks(ticks=[0, 1, 2, 3], labels=['Springger', 'Summer', 'Fall', 'Winter'])
    st.pyplot(plt)

elif plot_type == "Workday":
    plt.figure(figsize=(10, 5))
    colors = ["#D3D3D3", "#72BCD4"]
    
    # Ensure 'workingday' column exists and contains valid values
    if 'workingday' in hour.columns and hour['workingday'].notna().all():
        data1 = hour.groupby(by='workingday').cnt.mean().sort_values(ascending=False).reset_index()
        sns.barplot(
            y="cnt",
            x="workingday",
            data=data1,
            palette=colors
        )
        plt.title("Number of Rental", loc="center", fontsize=15)
        plt.ylabel(None)
        plt.xlabel(None)
        plt.xticks(ticks=[0, 1], labels=['Holiday', 'Workday'])
        st.pyplot(plt)
    else:
        st.error("Column 'workingday' contains invalid or missing values.")

st.pyplot(fig)
