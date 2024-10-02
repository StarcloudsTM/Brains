from sklearn.decomposition import PCA

# Sample Data
X = np.random.rand(100, 5)

# PCA with 2 components
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

print(X_reduced)
