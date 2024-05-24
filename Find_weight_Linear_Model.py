#Linear model Quiz 2 Lecture 5

import numpy as np

# Given data points
X = np.array([1, 3, 4])
y = np.array([2, 5, 6])

# Add a column of ones to X to account for the intercept term (b)
X_b = np.vstack([np.ones(X.shape[0]), X]).T

# Compute the optimal values of b and a using the normal equation
# w = (X_b.T * X_b)^(-1) * X_b.T * y
w = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y

# Extract the intercept (b) and slope (a)
b, a = w

print(f"b (intercept) = {b}")
print(f"a (slope) = {a}")

# Compute the prediction for x = 5
x_new = 5
y_pred = b + a * x_new

print(f"Prediction for x = {x_new}: y = {y_pred}")

# Determine the answer choice
if y_pred == 6.5:
    answer = 'A. 6.5'
elif y_pred == 7:
    answer = 'B. 7'
elif y_pred == 7.5:
    answer = 'C. 7.5'
elif y_pred == 8:
    answer = 'D. 8'
else:
    answer = 'E. Don’t know'

print(f"Answer: {answer}")