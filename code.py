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
