import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('vehicles_us (2).csv')

# App header
st.header('🚗 Hilarious Vehicle Sales Insights 🚗')

# Checkbox to display raw data 
if st.checkbox('Show Raw Data'):
    st.write(df.head())

# Histogram section with a humorous twist
st.subheader('Histogram of Laughter Levels in Vehicle Ads')

# Generate a random histogram (purely fictional!)
laughter_levels = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
hist_data = {'Laughter Levels': laughter_levels}
hist_df = pd.DataFrame(hist_data)
histogram = px.histogram(hist_df, x='Laughter Levels', title='Distribution of Laughter Levels')

# Display the histogram
st.plotly_chart(histogram)

# Scatter plot section with a humorous twist
st.subheader('Scatter Plot: Relationship Between Model and Condition')

# Generate a scatter plot with fictional data
model = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140]
condition = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
scatter_data = {'Model': model, 'Condition': condition}
scatter_df = pd.DataFrame(scatter_data)
scatter_plot = px.scatter(scatter_df, x='Model', y='Condition', title='Model vs Conditon - A Wild Connection')

# Display the scatter plot
st.plotly_chart(scatter_plot)

# Bar chart section with insights
st.subheader('Bar Chart: Most Common Vehicle Types')

# Generate a bar chart based on vehicle types
vehicle_types = df['type'].value_counts().reset_index()
vehicle_types.columns = ['Vehicle Type', 'Count']
bar_chart = px.bar(vehicle_types, x='Vehicle Type', y='Count', title='Most Common Vehicle Types')

# Display the bar chart
st.plotly_chart(bar_chart)

# Pie chart section with more insights
st.subheader('Pie Chart: Distribution of Drivetrains')

# Generate a pie chart based on paint color
type_distribution = df['paint_color'].value_counts().reset_index()
type_distribution.columns = ['Vehicle paint_color', 'Count']
pie_chart = px.pie(type_distribution, names='paint_colors', values='Count', title='Distribution of Vehicle Types')

# Display the pie chart
st.plotly_chart(pie_chart)

# A humorous footer
st.markdown("---")
st.markdown("This app is brought to you by the Department of Silly Statistics. All data is entirely fictional, "
            "and any resemblance to real vehicles or sales figures is purely coincidental. 🚙🤣")