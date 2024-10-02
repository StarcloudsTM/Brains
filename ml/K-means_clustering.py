from sklearn.cluster import KMeans

# Sample Data
X = np.random.rand(100, 2)

# Model
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# Cluster centers
print(kmeans.cluster_centers_)
