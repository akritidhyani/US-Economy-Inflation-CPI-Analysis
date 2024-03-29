# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jOtM8YMHUpfUUmZJC6DPYVp0A_v8pOFB
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV data into a Pandas DataFrame
csv_file_path = '/content/Inflation rate US.csv'  # Replace with the actual path to your CSV file
df = pd.read_csv(csv_file_path)

# Assuming your CSV has columns 'x' and 'y', adjust accordingly
x_values = df['YEAR']
y_values = df['AVG VALUE']

# Plot the data
plt.plot(x_values, y_values, linestyle='-', color='b', marker='*')
plt.title('Inflation Rate')
plt.xlabel('Year')
plt.ylabel('Rate')
plt.show()

file_path = '/content/Housing.csv'  # Replace with the actual path to your CSV file
df = pd.read_csv(file_path)
# Create a Seaborn bar plot
sns.barplot(x='Housing', y='Year', data=df, orient='h')

# Set labels and title
plt.xlabel('CPI(Housing)')
plt.ylabel('Year')
plt.title('Annual CPI for All Urban Consumers: Housing in U.S.')

# Show the plot
plt.show()

file_path = '/content/Med.csv'  # Replace with the actual path to your CSV file
df = pd.read_csv(file_path)

# Create a Seaborn bar plot
sns.set(style="whitegrid")
sns.barplot(x='Year', y='AVG CPI(Med)', data=df)

# Customize the plot using Matplotlib functions
plt.title('Annual CPI for All Urban Consumers: Medical Care in U.S.')
plt.xlabel('Year')
plt.ylabel('CPI(Medical Care)')

# Show the plot
plt.show()

df = pd.read_csv('/content/indicators.csv')
df_melted = pd.melt(df, id_vars=['Data Series'], var_name='Month', value_name='Value')
sns.set(style="whitegrid")
sns.lineplot(x='Month', y='Value', hue='Data Series', data=df_melted, marker='o')

# Customize the plot using Matplotlib functions
plt.title('Economic Indicators Over Time')
plt.xlabel('Time')
plt.ylabel('Values')
plt.legend(title='Data Series', loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True)
plt.ylim([-1,1])
# Show the plot
plt.show()

df = pd.read_csv('/content/Unemployment.csv')
df_melted = pd.melt(df, id_vars=['Data Series'], var_name='Month', value_name='Value')
sns.set(style="whitegrid")
sns.lineplot(x='Month', y='Value', hue='Data Series', data=df_melted, marker='o')

# Customize the plot using Matplotlib functions
plt.title('Unemployment Rate')
plt.xlabel('Time')
plt.ylabel('Values')
plt.ylim([3,4])
plt.grid(True)

# Show the plot
plt.show()