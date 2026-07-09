import numpy as np

def least_squares(A, b):
    A, b = np.array(A), np.array(b)
    return np.linalg.pinv(A.T @ A) @ A.T @ b