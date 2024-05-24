import numpy as np
#EXERCISE 14 SPRING 21
# Observations in each node
y_v1 = np.array([23.0])  # Only observation 4
y_v2 = np.array([10, 12, 13, 14])  # Observations 5, 6, 7, 8
y_v0 = np.concatenate((y_v1, y_v2))  # All observations for base node

# Function to calculate impurity given specific values
def calculate_impurity(data):
    if len(data) == 0:
        return 0
    mean_y = np.mean(data)
    impurity = np.sum((data - mean_y) ** 2) / len(data)
    return impurity

# Calculate the impurities dynamically
I_v0 = calculate_impurity(y_v0)  # Calculate impurity for v0
I_v1 = calculate_impurity(y_v1)  # Calculate impurity for v1
I_v2 = calculate_impurity(y_v2)  # Calculate impurity for v2

# Total number of observations in each node
N_v0 = len(y_v0)
N_v1 = len(y_v1)
N_v2 = len(y_v2)

# Calculate the impurity gain
impurity_gain = I_v0 - (N_v1 / N_v0) * I_v1 - (N_v2 / N_v0) * I_v2

print(f"Impurity of v0: {I_v0}")
print(f"Impurity of v1: {I_v1}")
print(f"Impurity of v2: {I_v2}")
print(f"Impurity Gain: {impurity_gain}")