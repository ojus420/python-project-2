import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the CSV file containing student performance data
# Replace 'student_performance.csv' with the path to your CSV file
data = pd.read_csv('student_performance.csv')

# Display the first few rows of the dataset
st.title('Student Performance Dashboard')
st.write("### Dataset Preview")
st.dataframe(data.head())

# Sidebar filters for interactive analysis
st.sidebar.header('Filter Options')
subject = st.sidebar.selectbox('Select a Subject', options=data['Subject'].unique())
grade_filter = st.sidebar.slider('Select Minimum Grade', min_value=int(data['Grade'].min()), 
                                 max_value=int(data['Grade'].max()), value=int(data['Grade'].min()))

# Filter the dataset based on the sidebar input
filtered_data = data[(data['Subject'] == subject) & (data['Grade'] >= grade_filter)]

# Display filtered data and summary statistics
st.write(f"### Summary for {subject} (Grades ≥ {grade_filter})")
st.write(filtered_data.describe())

# Plot a histogram of student grades
st.write("### Distribution of Grades")
plt.figure(figsize=(10, 6))
sns.histplot(data['Grade'], kde=True, color='skyblue')
plt.title('Grade Distribution')
plt.xlabel('Grade')
plt.ylabel('Frequency')
st.pyplot(plt)

# Plot a bar chart for average grades by subject
st.write("### Average Grade by Subject")
avg_grades = data.groupby('Subject')['Grade'].mean().sort_values()
plt.figure(figsize=(12, 6))
sns.barplot(x=avg_grades.index, y=avg_grades.values, palette='viridis')
plt.title('Average Grade by Subject')
plt.xlabel('Subject')
plt.ylabel('Average Grade')
st.pyplot(plt)

# Display a scatter plot for grades vs study hours (example of another analysis)
if 'Study_Hours' in data.columns:
    st.write("### Study Hours vs Grade")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Study_Hours', y='Grade', data=data, hue='Subject')
    plt.title('Study Hours vs Grade')
    plt.xlabel('Study Hours')
    plt.ylabel('Grade')
    st.pyplot(plt)

# Footer
st.write("### End of Dashboard")
st.write("This dashboard provides an overview of student performance data.")
