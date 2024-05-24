#Find prediction based on weights. Assume y is classified as 1 and x's value is selected to be 1


import numpy as np
def relu(z):
    return np.maximum(0, z)
def tanh(z):
    return np.tanh(z)

def linear(z):
    return z



# Sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Calculate predicted y_hat
def calculate_y_hat(x8, weights):
    # Add a constant feature to x8
    x8_tilde = np.array([1, x8])
    
    # Calculate dot product of x8_tilde and weights
    z = np.dot(x8_tilde, weights)
    
    # Calculate p(y=1|x8)
    p_y1_x8 = sigmoid(z)
    
    return p_y1_x8

# Define x8 and weights for each option
x8 = 1
options = {
    'A': [-0.93, 1.72],
    'B': [-2.82, 0.0],
    'C': [1.36, 0.4],
    'D': [-0.65, 0.0]
}

# Iterate over each option
for option, weights in options.items():
    y_hat = calculate_y_hat(x8, weights)
    print(f"For option {option}: Predicted y_hat = {y_hat:.2f}")