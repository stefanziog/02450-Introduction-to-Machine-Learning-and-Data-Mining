import numpy as np

def adaboost(delta, rounds):
    # Initial weights
    delta = np.array(delta)
    n = len(delta)
    weights = np.ones(n) / n

    # Run all rounds
    for i in range(rounds):
        eps = np.mean(delta == 1)
        alpha = 0.5 * np.log((1 - eps) / eps)
        s = np.array([-1 if d == 0 else 1 for d in delta])

        # Calculate weight vector and normalize it
        weights = weights.T * np.exp(s * alpha)
        weights /= np.sum(weights)

        # Print resulting weights
    for i, w in enumerate(weights):
        print('w[%i]: %f' % (i, w))
delta = [0,0,1,0,0,0,0 ]  # Example where 1 represents misclassification
rounds = 1  # Number of rounds to run AdaBoost

# Call the adaboost function with these parameters
adaboost(delta, rounds)

### NAIVE BAYES PROB
def naive_bayes(y, x, *obs):
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
            probs[i, j] = sum((X[:, j] == x[j]) & (y == c)) / sum(y == c)

    # Joint probs
    joint = np.prod(probs, axis=1)

    # Naive bayes
    return (joint * priors) / sum(joint * priors)


# ### Confusion Matrix
def confusion_matrix(matrix=None, tp=None, fn=None, tn=None, fp=None):
    if matrix:
        [tp, fn], [fp, tn] = matrix

    print("TP:", tp, "FN:", fn, "TN:", tn, "FP:", fp)

    n = tp + fn + tn + fp
    accuracy = (tp + tn) / n
    error = 1 - accuracy
    recall = tp / (tp + fn)
    prec = tp / (tp + fp)
    fpr = fp / (fp + tn)
    tpr = tp / (tp + fn)

    print('Accuracy:', accuracy)
    print('Error rate:', error)
    print('Recall:', recall)
    print('Precision:', prec)
    print('FPR:', fpr)
    print('TPR:', tpr)

### SUPPORT
def supp(A):
    A = np.array(A)
    return sum(A.all(axis=0)) / len(A[0])

### CONFIDENCE
def conf(A, B):
    AB = np.concatenate((A, B))
    return supp(AB) / supp(A)

### LIFT
def lift(A, B): return conf(A, B) / supp(B)

### DENSITY FOR ARD
def density(d):
    return 1 / d.mean()

### SIMILIARITY MEASURES
def sim(x, y):
    f11 = sum((x == 1) & (y == 1))
    f10 = sum((x == 1) & (y == 0))
    f01 = sum((x == 0) & (y == 1))
    f00 = sum((x == 0) & (y == 0))
    return f11, f10, f01, f00


def SMC(x, y):
    f11, f10, f01, f00 = sim(x, y)
    M = len(x)
    return (f11 + f00) / M


def Jaccard(x, y):
    f11, f10, f01, f00 = sim(x, y)
    return f11 / (f11 + f10 + f01)


def cos(x, y):
    f11, f10, f01, f00 = sim(x, y)
    return f11 / (np.linalg.norm(x) * np.linalg.norm(y))


def EJ(x, y):
    a = x.T * y
    b = np.linalg.norm(x) ** 2 + np.linalg.norm(y) ** 2 - a
    return a / b


# Impurity measures
def gini(v): return 1 - ((v / sum(v)) ** 2).sum()

def class_error(v): return 1 - v[np.argmax(v)] / v.sum()

Z = np.array([1,1,1,1,0,0,0,0,0,0])
Q = np.array([1,1,1,1,2,1,1,1,1,3])
SMC(Z, Q)
Jaccard(Z, Q)
cos(Z, Q)
print("SMC:", SMC(Z, Q))
print("Jaccard:", Jaccard(Z, Q))
print("Cosine:", cos(Z, Q))

# Vocabulary: ['hard', 'not', 'representation', 'bag', 'should', 'the', 'of', 'vector', 'give', 'time', 'you', 'a', 'be', 'words', 'remember']
# BoW Vector for s1: [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0]
# BoW Vector for s2: [0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1]

data_str = """
1 1 0 0 0 1 0 0 0 1
1 0 0 0 0 0 0 0 0 0
1 1 0 0 0 1 0 0 0 1
0 1 1 1 0 0 0 1 1 0
1 1 0 0 0 1 0 0 0 1
0 1 1 1 0 0 1 1 1 0
1 1 1 0 0 1 1 1 1 0
0 1 1 1 0 1 1 0 0 1
0 0 0 0 1 1 1 0 1 1
1 0 0 0 0 1 1 1 1 0
"""

# # Parse the data string into a NumPy array
# matrix_b2 = [[1], [1], [1], [0],[1],[0],[1],[0],[0],[1]]

# supp(matrix_b2)

# print(supp(matrix_b2))
 