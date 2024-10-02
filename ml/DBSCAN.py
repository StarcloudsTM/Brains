from sklearn.cluster import DBSCAN

# Sample Data
X = np.random.rand(100, 2)

# Model
db = DBSCAN(eps=0.3, min_samples=10).fit(X)

# Cluster labels
print(db.labels_)
