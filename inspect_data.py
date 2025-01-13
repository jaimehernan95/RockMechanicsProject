import pandas as pd
# Understanding the Machine Learning Model Setup
# Goal: Predict UCS (Unconfined Compressive Strength) based on rock properties.
# Features: density, porosity, mineral_content
# Target: UCS (Unconfined Compressive Strength)

# Load the dataset
data = pd.read_csv('data/rock_properties.csv')

# Check the first few rows
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Summary statistics
print(data.describe())
