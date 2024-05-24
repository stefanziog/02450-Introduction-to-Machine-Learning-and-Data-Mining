import numpy as np

def matrix_multiply(matrix_a, matrix_b):
    # Convert lists to numpy arrays
    a = np.array(matrix_a)
    b = np.array(matrix_b)

    # Check if the number of columns in the first matrix is equal to the number of rows in the second
    if a.shape[1] != b.shape[0]:
        raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second matrix.")
    
    # Multiply the matrices
    result = np.dot(a, b)
    print(result)
    return result

# Define the matrices
matrix_a = [[1, 2, 3], [4, 5, 6]]
matrix_b = [[7, 8], [9, 10], [11, 12]]

matrix_a1 = [[1.21, 0.05, -1.43, -0.43, -0.59]]
matrix_b1 = [[-0.47], [0.0], [-0.31], [-0.58],[-0.61]]
matrix_b2 = [[0.52], [0.44], [-0.73], [-0.04],[0.01]]
matrix_b3 = [[-0.24],[0.90], [0.37], [-0.01], [0.01]]

matrix_multiply(matrix_a1, matrix_b1)  # Perform matrix multiplication
matrix_multiply(matrix_a1, matrix_b2)  # Perform matrix multiplication
matrix_multiply(matrix_a1, matrix_b3)
# Perform matrix multiplication


#FOR MODELS AND TIME K1(K2*S+1)