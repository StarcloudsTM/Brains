from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# Sample Data
X = np.random.rand(20, 2)

# Hierarchical Clustering
Z = linkage(X, 'ward')

# Dendrogram
dendrogram(Z)
plt.show()
