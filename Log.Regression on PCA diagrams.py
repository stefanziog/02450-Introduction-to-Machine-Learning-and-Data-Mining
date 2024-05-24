import numpy as np
import matplotlib.pyplot as plt

# Define the sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Define the transformation functions
def transform1(b):
    return np.array([1, b[0]*2, b[1]*3])

def transform2(b):
    return np.array([1, b[0]*3, b[1]*2])

# Define the weight vectors
w1 = np.array([0.31, -0.06, 0.07])
w2 = np.array([0.72, 3.13, -0.25])

# Define the combinations
combinations = [
    (w1, transform1),
    (w2, transform1),
    (w1, transform2),
    (w2, transform2)
]

# Define test points
test_points = [np.array([2, 0]), np.array([-2, 0])]

# Evaluate classifiers at the test points
def evaluate_classifier(w, transform, points):
    return [sigmoid(np.dot(w, transform(point))) for point in points]

# Store results
results = []

for i, (w, transform) in enumerate(combinations):
    result = evaluate_classifier(w, transform, test_points)
    results.append((i+1, result))

# Print results
for i, result in results:
    print(f"Combination {i}: {result}")

# Visualization
x_min, x_max = -3, 3
y_min, y_max = -3, 3
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 500), np.linspace(y_min, y_max, 500))

def plot_decision_boundary(w, transform, ax, title):
    Z = np.array([sigmoid(np.dot(w, transform([x, y]))) for x, y in zip(np.ravel(xx), np.ravel(yy))])
    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, alpha=0.8)
    ax.scatter([2, -2], [0, 0], c='red', marker='x')
    ax.set_title(title)
    ax.set_xlim(xx.min(), xx.max())
    ax.set_ylim(yy.min(), yy.max())

fig, axs = plt.subplots(2, 2, figsize=(12, 10))
titles = ["Combination 1: w1 and transform1", "Combination 2: w2 and transform1",
          "Combination 3: w1 and transform2", "Combination 4: w2 and transform2"]

for i, (w, transform) in enumerate(combinations):
    plot_decision_boundary(w, transform, axs[i // 2, i % 2], titles[i])

plt.tight_layout()
plt.show()