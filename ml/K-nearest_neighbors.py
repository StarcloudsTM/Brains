from sklearn.neighbors import KNeighborsClassifier

# Sample Data
X = np.random.rand(50, 3)
y = np.random.randint(0, 2, 50)

# Model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Prediction
print(model.predict([[0.1, 0.2, 0.3]]))
