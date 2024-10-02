import numpy as np
from sklearn.linear_model import LinearRegression

# Sample Data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 3, 3, 2, 5])

# Model
model = LinearRegression()
model.fit(X, y)

# Prediction
prediction = model.predict([[6]])
print(prediction)
