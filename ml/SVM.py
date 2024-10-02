from sklearn.svm import SVC

# Sample Data
X = np.random.rand(150, 2)
y = np.random.randint(0, 2, 150)

# Model
model = SVC(kernel='linear')
model.fit(X, y)

# Prediction
print(model.predict([[0.1, 0.2]]))
