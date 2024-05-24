import numpy as np
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Your dataset
data = np.array([5.7, 6.0, 6.2, 6.3, 6.4, 6.6, 6.7, 6.9, 7.0, 7.4]).reshape(-1, 1)



# Generate the linkage matrix using 'average' method
Z = linkage(data, 'average')

# Create a dendrogram
dendrogram(Z, labels=data.flatten().astype(str), leaf_rotation=90)

plt.title('Hierarchical Clustering Dendrogram (Average linkage)')
plt.xlabel('Data point')
plt.ylabel('Distance')
plt.show()