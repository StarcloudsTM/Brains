from sklearn.linear_model import Ridge

# Sample Data
X = np.random.rand(100, 3)
y = np.random.rand(100)

# Model
ridge = Ridge(alpha=1.0)
ridge.fit(X, y)

# Prediction
print(ridge.predict([[0.1, 0.2, 0.3]]))
