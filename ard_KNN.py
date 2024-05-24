import numpy as np
#from scipy.spatial import distance

# Given 'scores' dataset
scores = np.array([5.7, 6.0, 6.2, 6.3, 6.4, 6.6, 6.7, 6.9, 7.0, 7.4])

def knn_density(scores, K, i):
    dists = np.abs(scores - scores[i])
    idx = np.argsort(dists)
    knn = idx[1:K+1]  # Exclude the i'th observation
    return 1 / np.mean(dists[knn])

def ard(scores, K, i):
    dists = np.abs(scores - scores[i])
    idx = np.argsort(dists)
    knn = idx[1:K+1]  # Exclude the i'th observation
    return knn_density(scores, K, i) / np.mean([knn_density(scores, K, j) for j in knn])

# Calculate the average relative density for observation O10 for K = 3 nearest neighbors
K = 3
i = 9
# i = 9  # Index of O10 in zero-based indexing
print(f"The average relative density for observation O10 for K = {K} nearest neighbors is {ard(scores, K, i)}")
