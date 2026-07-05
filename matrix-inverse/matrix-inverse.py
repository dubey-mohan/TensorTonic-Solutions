import numpy as np

def matrix_inverse(A):
    A = np.array(A)
    m, n = len(A), len(A[0])
    det = np.linalg.det(A)
    if det == 0 or m != n:
        return None
    return np.linalg.inv(A)
    
    
