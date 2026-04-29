import numpy as np

def split(matrix):
    """Splits a matrix into four quarters."""
    row, col = matrix.shape
    row2, col2 = row // 2, col // 2
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]

def strassen(a, b):
    """Recursive function to multiply two matrices using Strassen's algorithm."""
    # Base case: if the matrix is 1x1
    if len(a) == 1:
        return a * b

    # Divide: Split matrices into quarters
    a11, a12, a21, a22 = split(a)
    b11, b12, b21, b22 = split(b)

    # Calculate the 7 Strassen sub-formulas (P1 to P7)
    p1 = strassen(a11, b12 - b22)  
    p2 = strassen(a11 + a12, b22)        
    p3 = strassen(a21 + a22, b11)        
    p4 = strassen(a22, b21 - b11)        
    p5 = strassen(a11 + a22, b11 + b22)  
    p6 = strassen(a12 - a22, b21 + b22)  
    p7 = strassen(a11 - a21, b11 + b12)  

    # Combine: Calculate the quadrants of the resulting matrix C
    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p1 + p5 - p3 - p7

    # Stack the quadrants back into a single matrix
    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
    return c

# --- Execution Logic ---
if __name__ == "__main__":
    # Example 2x2 matrices
    matrix_a = np.array([[1, 2], [3, 4]])
    matrix_b = np.array([[5, 6], [7, 8]])

    print("Matrix A:\n", matrix_a)
    print("Matrix B:\n", matrix_b)
    
    result = strassen(matrix_a, matrix_b)
    print("\nResult of Strassen's Multiplication:\n", result)