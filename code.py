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

