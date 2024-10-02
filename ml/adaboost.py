from sklearn.ensemble import AdaBoostClassifier

# Sample Data
X = np.random.rand(80, 2)
y = np.random.randint(0, 2, 80)

# Model
model = AdaBoostClassifier(n_estimators=50)
model.fit(X, y)

# Prediction
print(model.predict([[0.1, 0.5]]))
