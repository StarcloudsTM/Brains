from sklearn.linear_model import Lasso

# Sample Data
X = np.random.rand(100, 3)
y = np.random.rand(100)

# Model
lasso = Lasso(alpha=0.1)
lasso.fit(X, y)

# Prediction
print(lasso.predict([[0.1, 0.2, 0.3]]))
