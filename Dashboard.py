# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 01:06:55 2025

@author: ACER
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')
day=pd.read_csv("Z:\Kuliah\Coding Camp\Bike-sharing-dataset\day.csv")
hour=pd.read_csv("Z:\Kuliah\Coding Camp\Bike-sharing-dataset\hour.csv")
datetime_columns = ['dteday']
for column in datetime_columns:
  hour[column] = pd.to_datetime(hour[column])
min_date = hour["dteday"].min()
max_date = hour["dteday"].max()
 
with st.sidebar:
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
main_df = hour[(hour["dteday"] >= str(start_date)) & 
                (hour["dteday"] <= str(end_date))]

st.header('Bike Rental Dashboard :sparkles:')

st.subheader("Highest Rental on Season and Hour")

# Create a figure and a set of subplots
fig, axes = plt.subplots(1, 2, figsize=(20, 5))

# Plot 1: Seasonal Rentals
colors = ["#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3"]
data1 = hour.groupby(by='season').cnt.mean().sort_values(ascending=False).reset_index() 
sns.barplot(y="cnt", x="season", data=data1, palette=colors, ax=axes[0])
axes[0].set_title("Number of Rental by Season", loc="center", fontsize=15)
axes[0].set_ylabel(None)
axes[0].set_xlabel(None)
axes[0].set_xticks(ticks=[0, 1, 2, 3], labels=['Spring', 'Summer', 'Fall', 'Winter'])

# Plot 2: Workday/Holiday Rentals
colors2 = ["#D3D3D3", "#72BCD4"]  # Colors for the second plot
data2 = hour.groupby(by='workingday').cnt.mean().sort_values(ascending=False).reset_index()
sns.barplot(y="cnt", x="workingday", data=data2, palette=colors2, ax=axes[1])
axes[1].set_title("Number of Rental by Workday/Holiday", loc="center", fontsize=15)
axes[1].set_ylabel(None)
axes[1].set_xlabel(None)
axes[1].set_xticks(ticks=[0, 1], labels=['Holiday', 'Workday'])

plt.tight_layout()
plt.show()

st.pyplot(fig)