import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import joblib  # Import joblib to save and load the model
from sklearn.metrics import mean_squared_error
import numpy as np

# Load dataset
data = pd.read_csv('data/rock_properties.csv')  
# Check the first few rows
print(data.head())

# Summary statistics
print(data.describe())

# Explore the dataset
print("Dataset Overview:")
print(data.describe())  # Summary statistics (e.g., mean, min, max, std)

# Optional: Get detailed information about the dataset
print("\nDataset Info:")
print(data.info())  # Info about the dataset, data types, non-null counts

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())  # Check for any missing values in the dataset

# Split data
X = data[['density', 'porosity', 'mineral_content']]  # Features
y = data['UCS']  # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'trained_model.pkl')  # Save the trained model to a file

# Load the model (optional, for future use)
# loaded_model = joblib.load('trained_model.pkl')

# Predict and evaluate
y_pred = model.predict(X_test)

# Calculate RMSE manually
mse = mean_squared_error(y_test, y_pred)  # Compute Mean Squared Error
rmse = np.sqrt(mse)  # Take the square root of MSE to get RMSE

# Output RMSE
print(f"Root Mean Squared Error: {rmse:.2f}")

# Create subplots for histograms
fig, axs = plt.subplots(2, 2, figsize=(10, 8))  # 2x2 grid of subplots

# Histogram for density
axs[0, 0].hist(data['density'], bins=10, color='skyblue', edgecolor='black')
axs[0, 0].set_title('Density Distribution')
axs[0, 0].set_xlabel('Density')
axs[0, 0].set_ylabel('Frequency')

# Histogram for porosity
axs[0, 1].hist(data['porosity'], bins=10, color='lightgreen', edgecolor='black')
axs[0, 1].set_title('Porosity Distribution')
axs[0, 1].set_xlabel('Porosity')
axs[0, 1].set_ylabel('Frequency')

# Histogram for mineral content
axs[1, 0].hist(data['mineral_content'], bins=10, color='lightcoral', edgecolor='black')
axs[1, 0].set_title('Mineral Content Distribution')
axs[1, 0].set_xlabel('Mineral Content')
axs[1, 0].set_ylabel('Frequency')

# Histogram for UCS
axs[1, 1].hist(data['UCS'], bins=10, color='lightskyblue', edgecolor='black')
axs[1, 1].set_title('UCS Distribution')
axs[1, 1].set_xlabel('UCS')
axs[1, 1].set_ylabel('Frequency')

# Adjust the layout to prevent overlap
plt.tight_layout()

# Show histograms
plt.show()

# Visualize the results (Actual vs Predicted UCS)
plt.figure(figsize=(6, 6))
plt.scatter(y_test, y_pred)
plt.xlabel("Actual UCS")
plt.ylabel("Predicted UCS")
plt.title("Actual vs Predicted UCS")
plt.show()