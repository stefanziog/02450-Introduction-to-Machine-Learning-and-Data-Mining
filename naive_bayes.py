import numpy as np
import pandas as p
import extended_toolbox as te  
import toolbox_02450 as tb
import exam_toolbox as ex

import numpy as np
from scipy.stats import norm

def naive_bayes_gaussian(y, x, *obs):
    y = np.array(y)
    classes = set(y)
    X = np.array(obs).T
    N, M = X.shape
    C = len(classes)
    priors = np.zeros(C)

    # Class priors
    for i, c in enumerate(classes):
        priors[i] = sum(y == c) / N

    # Probs
    probs = np.zeros((C, M))
    for i, c in enumerate(classes):
        for j in range(M):
            # Calculate mean and standard deviation
            mu = np.mean(X[y == c, j])
            sigma = np.sqrt(400)  # Given in the problem

            # Calculate Gaussian PDF
            probs[i, j] = norm.pdf(x[j], mu, sigma)

    # Joint probs
    joint = np.prod(probs, axis=1)

    # Naive bayes
    return (joint * priors) / sum(joint * priors)

labels = ['f%i' % (i%3 + 1) for i in range(1,12)]  

data_str = """
38.0 15.1 27.4 77.9 18.1 33.3 48.5 50.0
26.8 12.8 52.0 77.0 22.5 68.1 66.0 75.0
64.5 39.6 74.4 37.1 45.7 66.7 66.0 64.3
63.2 45.7 29.1 41.4 49.1 56.9 59.2 50.0
66.3 34.3 37.7 43.1 40.9 63.9 70.9 60.7
56.7 34.7 72.2 47.3 38.4 61.1 62.1 55.4
63.4 30.6 66.4 49.8 30.2 62.5 50.5 42.9
87.1 85.3 19.3 19.2 68.6 34.7 64.1 33.9
51.3 46.8 14.8 53.4 49.3 37.5 52.4 35.7
67.5 62.3 13.0 33.2 66.7 51.4 41.7 39.3
86.0 71.3 25.1 20.5 71.9 25.0 48.5 32.1

"""

lines = data_str.strip().split('\n')

# Split each line into values and convert them to floats
data = [[float(value) for value in line.split()[1:]] for line in lines]

data = np.array(data)

# Test sample
x = [32.0, 14.0]

# Call the function
probs = naive_bayes_gaussian(labels, x, *data.T)