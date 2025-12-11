import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Data loading 

# Try loading dataset
try:
    df = pd.read_csv("Expanded_data_with_more_features.csv")   # Read CSV
    print("Dataset loaded successfully!")                      # Success msg
    print(df.head())                                           # Show sample
except FileNotFoundError:                                      # File missing
    print("Error: File not found. Please check the filename or path.")
except Exception as e:                                         # Other errors
    print("An unexpected error occurred:", e)
# ==============================
# BLOCK 1: OVERVIEW & DUPLICATES
# ==============================

# 1. Overview in Table Format
overview = pd.DataFrame({
    'Column': df.columns,
    'Data Type': df.dtypes.astype(str),   # convert dtypes to string for display
    'Missing Values': df.isnull().sum()
})
print("=== Dataset Overview ===")
print(overview.to_string(index=False))  # Safe display in all environments

# 2. Remove Duplicates
duplicates = df.duplicated().sum()
print(f"\nNumber of duplicate rows removed: {duplicates}")
df = df.drop_duplicates()

# 3. Verify Changes (Aligned)
cleaned_overview = pd.DataFrame({
    'Column': df.columns,
    'Data Type': df.dtypes.astype(str),
    'Missing Values After Cleaning': df.isnull().sum()
})
print("\n=== Cleaned Dataset Overview ===")
print(cleaned_overview.to_string(index=False))
print("\nData Shape after cleaning:", df.shape)
# 1. Standardize Text Columns
text_cols = categorical_cols  # same as above
for col in text_cols:
    df[col] = df[col].str.lower().str.strip()
# Total Score
df['TotalScore'] = df['MathScore'] + df['ReadingScore'] + df['WritingScore']
# Average Score
df['AvgScore'] = df['TotalScore'] / 3
# 3. Final Check
print("\nCleaned Data Overview:")
print(df.info())
print(df.head())

#Distribution of Scores

plt.figure(figsize=(8,6))                                                             # Set figure size
sns.histplot(df['MathScore'], kde=True, color='skyblue', label='Math Score')              # MathScore distribution
sns.histplot(df['ReadingScore'], kde=True, color='lightgreen', label='Reading Score')      # ReadingScore distribution
sns.histplot(df['WritingScore'], kde=True, color='salmon', label='Writing Score')        # WritingScore distribution
plt.title('Distribution of Exam Scores')                                                 # Chart title
plt.xlabel('Scores')                          # X-axis label
plt.ylabel('Frequency')                  # Y-axis label
plt.legend()                     # Display legend
plt.show()                     # Show plot

# relation bw Study Hours and Total Score

df['TotalScore'] = df['MathScore'] + df['ReadingScore'] + df['WritingScore']       # Calculate total score
plt.figure(figsize=(6,4))                                                          # Set figure size
sns.scatterplot(data=df, x='WklyStudyHours', y='TotalScore', hue='TestPrep')       # Scatter: study hours vs total score
plt.title('Weekly Study Hours vs Total Score')                                      # Add plot title
plt.xlabel('Weekly Study Hours')                                             # X-axis label
plt.ylabel('Total Score')                                               # Y-axis label
plt.show()                                                          # Display plot

avg_gender = df.groupby('Gender')[['MathScore', 'ReadingScore', 'WritingScore']].mean()
print(avg_gender)

avg_gender.plot(kind='bar', figsize=(6,4))
plt.title('Average Score by Gender')
plt.ylabel('Average Score')
plt.show()

avg_prep = df.groupby('TestPrep')[['MathScore', 'ReadingScore', 'WritingScore']].mean()
print(avg_prep)

avg_prep.plot(kind='bar', figsize=(6,3), color=['skyblue', 'lightgreen', 'salmon'])
plt.title('Impact of Test Preparation on Scores')
plt.ylabel('Average Score')
plt.show()

import pandas as pd
#  Total Marks
df['TotalMarks'] = df[['MathScore', 'ReadingScore', 'WritingScore']].sum(axis=1)

#  Class Average per student
df['ClassAverage'] = df[['MathScore', 'ReadingScore', 'WritingScore']].mean(axis=1)

# Percentage
df['Percentage'] = (df['TotalMarks'] / 300) * 100  # assuming each subject is out of 100

# Display in one table (separate columns)
output1 = df[['TotalMarks', 'ClassAverage', 'Percentage']]
print("=== Total, Class Average & Percentage ===")
display(output1)

#Grading System

# Grade Assignment based on Percentage
def assign_grade(perc):
    if perc >= 90:
        return 'A+'  # Excellent
    elif perc >= 80:
        return 'A'   # Very Good
    elif perc >= 70:
        return 'B'   # Good
    elif perc >= 60:
        return 'C'   # Average
    elif perc >= 50:
        return 'D'   # Pass
    else:
        return 'F'   # Fail

df['Grade'] = df['Percentage'].apply(assign_grade)                   # Apply grade to each student
# Class Rank based on TotalMarks
df['ClassRank'] = df['TotalMarks'].rank(ascending=False, method='min')              # Rank students
# Display results in a table
output2 = df[['Grade', 'ClassRank']]                          # Select only Grade and Rank columns
print("=== Grade & Class Rank ===")
display(output2)  # Show table


