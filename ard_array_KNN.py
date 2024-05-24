import numpy as np

# Input data as a multi-line string
data = """
0.0 3.7 3.4 2.3 1.8 1.6 2.4 2.6 2.5 4.3
3.7 0.0 3.2 5.1 3.5 2.9 4.4 4.6 4.0 7.2
3.4 3.2 0.0 4.1 2.6 4.0 2.7 5.3 2.9 6.1
2.3 5.1 4.1 0.0 3.7 3.2 1.7 2.7 1.9 2.6
1.8 3.5 2.6 3.7 0.0 2.8 3.2 4.4 3.4 5.6
1.6 2.9 4.0 3.2 2.8 0.0 3.4 2.1 3.1 5.3
2.4 4.4 2.7 1.7 3.2 3.4 0.0 3.8 0.8 4.1
2.6 4.6 5.3 2.7 4.4 2.1 3.8 0.0 3.5 4.0
2.5 4.0 2.9 1.9 3.4 3.1 0.8 3.5 0.0 4.4
4.3 7.2 6.1 2.6 5.6 5.3 4.1 4.0 4.4 0.0

"""



# Convert the multi-line string into a NumPy array of floats
distances = np.array([list(map(float, line.split())) for line in data.strip().split('\n')])

def knn_density(distances, K, i):
    dists = distances[i]
    idx = np.argsort(dists)
    knn = idx[1:K+1]  # Exclude the i'th observation because the distance to itself is zero
    
    return 1 / np.mean(dists[knn])

def ard(distances, K, i):
    dists = distances[i]
    idx = np.argsort(dists)
    knn = idx[1:K+1]  # Exclude the i'th observation
    return knn_density(distances, K, i) / np.mean([knn_density(distances, K, j) for j in knn])

# Calculate the average relative density for observation 4 (index 3 in zero-based indexing) for K = 2 nearest neighbors
K = 3
i = 0  # Index of the fourth observation in zero-based indexing
density = knn_density(distances, K, i)
average_relative_density = ard(distances, K, i)
print(f"The density for observation O4 for K = {K} nearest neighbors is {density}")
print(f"The average relative density for observation O4 for K = {K} nearest neighbors is {average_relative_density}")


