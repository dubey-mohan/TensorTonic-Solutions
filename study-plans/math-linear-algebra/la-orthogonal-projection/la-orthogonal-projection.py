import numpy as np

def projection_matrix(A):
    A = np.array(A)
    return A @ np.linalg.pinv(A)
   