import numpy as np
#KMEANS 2
def kmeans2_main(data, y, centroids):
    c1, c2 = centroids
    cat1, cat2 = [], []

    for i in range(0, len(data)):
        if abs(data[i] - c1) <= abs(data[i] - c2):
            cat1.append((data[i], y[i]))
        else:
            cat2.append((data[i], y[i]))

    # Print clusterings
    print("Cluster 1:", cat1)
    print("Cluster 2:", cat2)

    # Return new centroids
    return np.array([np.mean([x[0] for x in cat1]), np.mean([x[0] for x in cat2])])

def kmeans2(data, y, centroids):
    current = np.array(centroids)
    old = np.zeros(2)
    while not np.allclose(current, old):
        old = current
        current = kmeans2_main(data, y, current)
    print("terminated!\ncentroids:", current)

# DATA HERE!!!
y = [0, 0, 0, 0, 1, 1, 1, 0, 0, 1]
scores = [5.7, 6.0, 6.2, 6.3, 6.4, 6.6, 6.7, 6.9, 7.0, 7.4]
initial_centroids = [6.0, 6.5]  # Adjust initial centroids as needed

#kmeans2(scores, y, initial_centroids)

#KMEANS3
def kmeans3_main(data, centroids):
    c1, c2, c3 = centroids
    dif1, dif2, dif3 = data - c1, data - c2, data - c3
    cat1, cat2, cat3 = [], [], []

    for i in range(0, len(data)):
        if abs(dif1[i]) <= abs(dif2[i]) and abs(dif1[i]) <= abs(dif3[i]):
            cat1.append(data[i])
        elif abs(dif2[i]) <= abs(dif1[i]) and abs(dif2[i]) <= abs(dif3[i]):
            cat2.append(data[i])
        elif abs(dif3[i]) <= abs(dif1[i]) and abs(dif3[i]) <= abs(dif2[i]):
            cat3.append(data[i])
        else:
            print("ERROR")

    # Print clusterings
    print(cat1, cat2, cat3)

    # Return new centroids
    return np.array([np.mean(cat1), np.mean(cat2), np.mean(cat3)])


def kmeans3(data, centroids):
    current = np.array(centroids)
    old = np.zeros(3)
    while np.any(current != old):
        old = current
        current = kmeans3_main(data, current)
    print("terminated!\ncentroids:", current)
    
#DATA KMEANS3
data = np.array([0.0, 2.0, 4.0, 5.0, 6.0, 7.0, 14.0])
initial_centroids_3 = [1.0, 5.0, 8.0]  # Adjust initial centroids as needed

kmeans3(data, initial_centroids_3)