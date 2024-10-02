from sklearn.ensemble import RandomForestClassifier

# Sample Data
X = np.random.rand(200, 5)
y = np.random.randint(0, 3, 200)

# Model
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# Prediction
print(model.predict([[0.1, 0.2, 0.3, 0.4, 0.5]]))
