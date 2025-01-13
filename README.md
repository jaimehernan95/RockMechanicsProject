# Rock Mechanics Prediction

## Overview:
This project aims to predict the Uniaxial Compressive Strength (UCS) of rocks using machine learning models. The dataset contains various rock properties such as density, porosity, and mineral content to train a model that can predict UCS.

## Dataset:
The dataset includes the following columns:
- **Density**: The mass per unit volume of the rock.
- **Porosity**: The ratio of the void space in the rock.
- **Mineral Content**: The percentage of minerals in the rock.
- **UCS (Uniaxial Compressive Strength)**: The strength of the rock under compression.

## Methodology:
1. **Data Exploration**: We loaded and explored the dataset, identifying the structure and summary statistics.
2. **Model Training**: A Random Forest model was trained to predict UCS based on the rock properties.
3. **Evaluation**: The model was evaluated using Root Mean Squared Error (RMSE) to assess its performance.

## Visuals:
- Scatter plot comparing actual vs. predicted UCS.
- Histograms showing the distribution of features such as density and porosity.

## Steps to Run:
1. Clone this repository:
   ```bash
   git clone https://github.com/jaimehernan95/RockMechanicsProject.git


## Visuals:
- Scatter plot comparing actual vs. predicted UCS.
- Histograms showing the distribution of features such as density and porosity.

### Distribution of Features
![Distribution of Features](images/Histogram-for-density-porosity-mineralCon-and-UCS.png)
## Interpretation of Results:

### 1. **Feature Distributions:**
   The histograms for **density**, **porosity**, **mineral content**, and **UCS** show the distribution of these features in the dataset. 
   - **Density**: The distribution of density values can provide insight into the mass-to-volume ratio of the rocks, which could influence UCS.
   - **Porosity**: Higher porosity often means lower strength in rocks, so the distribution of porosity values helps us understand its effect on the compressive strength.
   - **Mineral Content**: This can directly impact the strength of the rock. Different minerals have different characteristics, and this histogram shows their distribution.

### 2. **Actual vs Predicted UCS:**
   The scatter plot compares the actual and predicted UCS values. Ideally, the points should form a diagonal line from the bottom left to the top right, indicating that the model is making accurate predictions. The closer the points are to this line, the better the model is performing.
