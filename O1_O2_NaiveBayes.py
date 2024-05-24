import numpy as np

# Data string
data_str = """
0 0 1 0
1 0 1 0
0 1 0 0
1 0 1 1
1 0 0 0
0 0 0 1
1 0 1 0
0 1 0 0
0 0 1 0
1 0 0 0
"""

# Parse the data string into a NumPy array
data = np.array([list(map(int, row.split())) for row in data_str.strip().split('\n')])

# Define the class labels
labels = np.array([1, 1, 1, 1, 1,1,2,2,2,2,])

# Specify the features to use (f1, (f2,f3), f4)
features = [0, (2,3),4]

# Observation
observation = [0,0,1,0]

# Function to calculate probabilities
def calculate_probabilities(data, labels, features):
    # Calculate prior probabilities
    classes, class_counts = np.unique(labels, return_counts=True)
    priors = {c: class_counts[i] / len(labels) for i, c in enumerate(classes)}

    # Initialize likelihoods
    likelihoods = {c: np.ones(len(features)) for c in classes}
    
    # Calculate likelihoods
    for i, feature in enumerate(features):
        for c in classes:
            class_data = data[labels == c]
            likelihoods[c][i] = np.sum(class_data[:, feature] == observation[i]) / len(class_data)
    
    return priors, likelihoods

# Function to calculate posterior probabilities
def calculate_posteriors(priors, likelihoods):
    posteriors = {}
    total_posterior = 0

    for c in priors:
        posterior = priors[c]
        for likelihood in likelihoods[c]:
            posterior *= likelihood
        posteriors[c] = posterior
        total_posterior += posterior

    # Normalize to get final probabilities
    for c in posteriors:
        posteriors[c] /= total_posterior
    
    return posteriors

# Calculate probabilities
priors, likelihoods = calculate_probabilities(data, labels, features)
posteriors = calculate_posteriors(priors, likelihoods)

# Output the probability that y = 1 (class C1)
print(f"Probability that y = 1: {posteriors[1]:.10f}")