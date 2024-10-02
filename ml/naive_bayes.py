from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix

# Sample Data
X = np.random.rand(100, 2)
y = np.random.randint(0, 2, 100)

# Model
model = GaussianNB()
model.fit(X, y)

# Prediction
y_pred = model.predict(X)
print(confusion_matrix(y, y_pred))
