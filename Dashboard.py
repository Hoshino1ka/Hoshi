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

url = 'https://raw.githubusercontent.com/Hoshino1ka/Hoshi/refs/heads/main/hour.csv'
hour = pd.read_csv(url)

hour['dteday'] = pd.to_datetime(hour['dteday'])

st.header('Bike Rental Dashboard :sparkles:')

date_range = st.date_input("Select Date Range", [hour['dteday'].min(), hour['dteday'].max()])
if len(date_range) == 2:
    start_date, end_date = date_range
    hour_filtered = hour[(hour['dteday'] >= pd.Timestamp(start_date)) & (hour['dteday'] <= pd.Timestamp(end_date))]
else:
    hour_filtered = hour

st.subheader("Highest Rental Based on Season and workday or not.")

plot_type = st.radio("Select plot type:", ("Season", "Workday"))

if plot_type == "Season":
    plt.figure(figsize=(10, 5))
    colors = ["#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3"]
    data1 = hour_filtered.groupby(by='season').cnt.mean().sort_values(ascending=False).reset_index()
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
    data1 = hour_filtered.groupby(by='workingday').cnt.mean().sort_values(ascending=False).reset_index()
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
