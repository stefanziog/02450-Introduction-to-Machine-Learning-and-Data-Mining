import numpy as np

# Initialize data
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
    print("centroids: ", c1, c2, c3)

    # Return new centroids
    return np.array([np.mean(cat1), np.mean(cat2), np.mean(cat3)])


def kmeans3(data, centroids):
    current = np.array(centroids)
    old = np.zeros(3)
    while np.any(current != old):
        old = current
        current = kmeans3_main(data, current)
    print("terminated!\ncentroids:", current)

# cent = [1, 5, 8]
# data = [0 ,2, 4, 5, 6, 7, 14]

# kmeans3(data, cent)


def kmeans2_main(data, centroids):
    c1, c2 = centroids
    dif1, dif2 = data - c1, data - c2
    cat1, cat2 = [], []

    for i in range(0, len(data)):
        if abs(dif1[i]) <= abs(dif2[i]):
            cat1.append(data[i])
        elif abs(dif2[i]) <= abs(dif1[i]):
            cat2.append(data[i])
        else:
            print("ERROR")

    # Print clusterings
    print(cat1, cat2)
    print("centroids: ", c1, c2)


    # Return new centroids
    return np.array([np.mean(cat1), np.mean(cat2)])


def kmeans2(data, centroids):
    current = np.array(centroids)
    old = np.zeros(2)
    while np.any(current != old):
        old = current
        current = kmeans2_main(data, current)
    print("terminated!\ncentroids:", current)
    
# Example data: A simple array of data points
data = np.array([2,4,6,9,10,11,13])

# # Initial centroids: Choose two distinct values
centroids = [1 ,6]

# # Call the k-means function
kmeans2(data, centroids)
    


def kmeans_main(data, centroids):
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


def kmeans(data, centroids):
    current = np.array(centroids)
    old = np.zeros(3)
    while np.any(current != old):
        old = current
        current = kmeans3_main(data, current)
    print("terminated!\ncentroids:", current)
    
    
    
    
    
    
def kmeans4_main(data, centroids):
    c1, c2, c3, c4 = centroids
    dif1, dif2, dif3, dif4 = data - c1, data - c2, data - c3, data - c4
    cat1, cat2, cat3, cat4 = [], [], [], []

    for i in range(0, len(data)):
        # Calculate distances and determine the nearest centroid
        distances = [abs(dif1[i]), abs(dif2[i]), abs(dif3[i]), abs(dif4[i])]
        min_index = distances.index(min(distances))
        
        if min_index == 0:
            cat1.append(data[i])
        elif min_index == 1:
            cat2.append(data[i])
        elif min_index == 2:
            cat3.append(data[i])
        elif min_index == 3:
            cat4.append(data[i])
        else:
            print("ERROR")

    # Print clusterings
    print(cat1, cat2, cat3, cat4)

    # Return new centroids
    return np.array([np.mean(cat1), np.mean(cat2), np.mean(cat3), np.mean(cat4)])

def kmeans4(data, centroids):
    current = np.array(centroids)
    old = np.zeros(4)  # Change the size to match the number of centroids
    while np.any(current != old):
        old = current
        current = kmeans4_main(data, current)
    print("terminated!\ncentroids:", current)

# Example data and initial centroids
# data = np.array([0.1, 0.3, 0.5, 1.0, 2.2, 3.0, 4.1, 4.4, 4.7])
# initial_centroids = np.array([0.2, 0.75, 3.1, 4.55])

# # Call the function
# kmeans4(data, initial_centroids)
