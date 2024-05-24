import numpy as np

# Function to generate the probability matrix
def generate_probability_matrix(P_clusters, Q_clusters):
    unique_P = sorted(set(P_clusters))
    unique_Q = sorted(set(Q_clusters))
    
    P_cluster_map = {cluster: idx for idx, cluster in enumerate(unique_P)}
    Q_cluster_map = {cluster: idx for idx, cluster in enumerate(unique_Q)}
    
    count_matrix = np.zeros((len(unique_P), len(unique_Q)))
    
    for P, Q in zip(P_clusters, Q_clusters):
        P_idx = P_cluster_map[P]
        Q_idx = Q_cluster_map[Q]
        count_matrix[P_idx, Q_idx] += 1
    
    N = len(P_clusters)
    probability_matrix = count_matrix / N
    
    return probability_matrix, N

# Function to calculate entropy
def entropy(probabilities):
    return -np.sum([p * np.log2(p) for p in probabilities if p > 0])

# Define the observations and their cluster assignments
P_clusters = [2, 3, 2, 1, 2, 1, 2, 2, 2, 2]  # Clusters according to P
Q_clusters = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3]  # Clusters according to Q

# Generate the probability matrix
probability_matrix, N = generate_probability_matrix(P_clusters, Q_clusters)

# Calculate the marginal probabilities p_P(i) and p_Q(j)
p_P = np.sum(probability_matrix, axis=1)
p_Q = np.sum(probability_matrix, axis=0)

# Calculate the entropy of P and Q
H_P = entropy(p_P)
H_Q = entropy(p_Q)

# Calculate the joint entropy H[P, Q]
joint_probabilities = probability_matrix
H_PQ = -np.sum([joint_probabilities[i, j] * np.log2(joint_probabilities[i, j]) 
                for i in range(probability_matrix.shape[0]) 
                for j in range(probability_matrix.shape[1]) 
                if joint_probabilities[i, j] > 0])

# Calculate the Mutual Information (MI)
MI = H_P + H_Q - H_PQ

# Calculate the Normalized Mutual Information (NMI)
NMI = MI / np.sqrt(H_P * H_Q)

# Print the results
print("Probability matrix:\n", probability_matrix)
print("Mutual Information (MI):", MI)
print("Normalized Mutual Information (NMI):", NMI)