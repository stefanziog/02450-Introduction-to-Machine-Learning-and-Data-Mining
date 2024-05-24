import math

# GINI IMPURITY 0,1 TABLES

# Given class probabilities at the root
p_C1_r = 2 / 11
p_C2_r = 5 / 11
p_C3_r = 4 / 11

# Given class probabilities for each child node after split
p_C1_v1 = 2 / 6
p_C2_v1 = 4 / 6
p_C3_v1 = 0 / 6

p_C1_v2 = 0 / 5
p_C2_v2 = 1 / 5
p_C3_v2 = 4 / 5

# Calculate Gini impurity for the root node
I_r = 1 - (p_C1_r**2 + p_C2_r**2 + p_C3_r**2)

# Calculate Gini impurity for each child node
I_v1 = 1 - (p_C1_v1**2 + p_C2_v1**2 + p_C3_v1**2)
I_v2 = 1 - (p_C1_v2**2 + p_C2_v2**2 + p_C3_v2**2)

# Calculate impurity gain
n1 = 6  # Number of observations in v1
n2 = 5  # Number of observations in v2
total_n = n1 + n2

impurity_gain = I_r - (n1 / total_n) * I_v1 - (n2 / total_n) * I_v2

print("FOR GINI IMPURITY",I_r, I_v1, I_v2, impurity_gain)

# FOR CLASSERRROR IMPURITY

# Given class probabilities at the root
p_C1_r = 119 / 333
p_C2_r = 68 / 333
p_C3_r = 68 / 333

# Given class probabilities for each child node after split
p_C1_v1 = 146 / 146
p_C2_v1 = 0 
p_C3_v1 = 68 / 68

p_C1_v2 = 0 / 5
p_C2_v2 = 1 / 5
p_C3_v2 = 4 / 5

# Calculate class error for the root node
I_r = 1 - max(p_C1_r, p_C2_r, p_C3_r)

# Calculate class error for each child node
I_v1 = 1 - max(p_C1_v1, p_C2_v1, p_C3_v1)
I_v2 = 1 - max(p_C1_v2, p_C2_v2, p_C3_v2)

# Calculate impurity gain (error reduction)
n1 = 6  # Number of observations in v1
n2 = 5  # Number of observations in v2
total_n = n1 + n2

error_reduction = I_r - (n1 / total_n) * I_v1 - (n2 / total_n) * I_v2

print("CLASSERROR",I_r, I_v1, I_v2, error_reduction)

# FOR ENTROPY IMPURITY

# Given class probabilities at the root
p_C1_r = 400 / 500
p_C2_r = 100 / 500

# Given class probabilities for each child node after split
p_C1_v1 = 2 / 6
p_C2_v1 = 4 / 6
p_C3_v1 = 0 / 6  # Since the class probability is 0, it won't contribute to entropy

p_C1_v2 = 0 / 5  # Since the class probability is 0, it won't contribute to entropy
p_C2_v2 = 1 / 5

# Helper function to calculate entropy
def entropy(*probs):
    return -sum(p * math.log2(p) for p in probs if p > 0)

# Calculate entropy for the root node
I_r = entropy(p_C1_r, p_C2_r, p_C3_r)
print("ENTROPY I_r",I_r)

# Calculate entropy for each child node
I_v1 = entropy(p_C1_v1, p_C2_v1, p_C3_v1)
I_v2 = entropy(p_C1_v2, p_C2_v2, p_C3_v2)

# Calculate impurity gain (information gain)
n1 = 6  # Number of observations in v1
n2 = 5  # Number of observations in v2
total_n = n1 + n2

information_gain = I_r - (n1 / total_n) * I_v1 - (n2 / total_n) * I_v2

print("ENTROPY IMPURITY",I_r, I_v1, I_v2, information_gain)