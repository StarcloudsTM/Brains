from xgboost import XGBClassifier

# Sample Data
X = np.random.rand(100, 3)
y = np.random.randint(0, 2, 100)

# Model
model = XGBClassifier()
model.fit(X, y)

# Prediction
print(model.predict([[0.1, 0.2, 0.3]]))
