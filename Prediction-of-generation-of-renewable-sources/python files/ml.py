import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load data into a pandas DataFrame
data = pd.read_csv("forecast.csv")

# Define input feature and output target
X = data[['input_feature']]
y = data['output_target']

# Train a linear regression model
model = LinearRegression()
model.fit(X, y)

# Make a prediction for a new input value
new_X = [[2.5]]
prediction = model.predict(new_X)

# Print predicted output
print(prediction)