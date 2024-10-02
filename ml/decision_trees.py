from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

# Sample Data
X = np.random.rand(150, 4)
y = np.random.randint(0, 3, 150)

# Model
tree = DecisionTreeClassifier()
tree.fit(X, y)

# Prediction
y_pred = tree.predict(X)
print(classification_report(y, y_pred))
