import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = 'daily_temp (1).csv'
data = pd.read_csv(file_path)

# Clean the data
data['날짜'] = data['날짜'].str.strip()
data['날짜'] = pd.to_datetime(data['날짜'], format='%Y-%m-%d')
data['연도'] = data['날짜'].dt.year

# Calculate yearly average minimum and maximum temperatures
yearly_data = data.groupby('연도').agg({
    '최저기온(℃)': 'mean',
    '최고기온(℃)': 'mean'
}).reset_index()

yearly_data.columns = ['연도', '평균최저기온(℃)', '평균최고기온(℃)']

# Streamlit app
st.title('Yearly Average Temperature Trends')

# Choose the type of graph
chart_type = st.selectbox("Choose chart type:", ["Line Chart", "Bar Chart"])

# Plotting
plt.figure(figsize=(10, 6))
if chart_type == "Line Chart":
    sns.lineplot(data=yearly_data, x='연도', y='평균최저기온(℃)', label='평균최저기온(℃)', marker='o')
    sns.lineplot(data=yearly_data, x='연도', y='평균최고기온(℃)', label='평균최고기온(℃)', marker='o')
    plt.ylabel('Temperature (℃)')
    plt.title('Yearly Average Minimum and Maximum Temperatures (Line Chart)')
elif chart_type == "Bar Chart":
    width = 0.35
    x = yearly_data['연도']
    plt.bar(x - width/2, yearly_data['평균최저기온(℃)'], width, label='평균최저기온(℃)')
    plt.bar(x + width/2, yearly_data['평균최고기온(℃)'], width, label='평균최고기온(℃)')
    plt.ylabel('Temperature (℃)')
    plt.title('Yearly Average Minimum and Maximum Temperatures (Bar Chart)')

plt.xlabel('Year')
plt.legend()
st.pyplot(plt)
