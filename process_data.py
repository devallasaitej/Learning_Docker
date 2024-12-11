import pandas as pd

# Example: Load data and print summary
data = pd.read_csv('data/reddit_sample.csv')

# Perform some operations
print(data.head())
print(data.describe())