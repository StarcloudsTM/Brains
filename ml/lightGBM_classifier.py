import lightgbm as lgb

# Sample Data
X = np.random.rand(200, 4)
y = np.random.randint(0, 2, 200)

# Model
train_data = lgb.Dataset(X, label=y)
param = {'objective': 'binary'}
model = lgb.train(param, train_data)

# Prediction
print(model.predict([[0.1, 0.2, 0.3, 0.4]]))
