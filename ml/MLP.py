from sklearn.neural_network import MLPClassifier

# Sample Data
X = np.random.rand(150, 4)
y = np.random.randint(0, 2, 150)

# Model
mlp = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=1000)
mlp.fit(X, y)

# Prediction
print(mlp.predict([[0.1, 0.2, 0.3, 0.4]]))
