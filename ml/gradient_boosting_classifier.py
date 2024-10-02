from sklearn.ensemble import GradientBoostingClassifier

# Sample Data
X = np.random.rand(100, 4)
y = np.random.randint(0, 2, 100)

# Model
model = GradientBoostingClassifier()
model.fit(X, y)

# Prediction
print(model.predict([[0.1, 0.2, 0.3, 0.4]]))
