import numpy as np

def pseudoinverse(A):
    A = np.array(A)
    return np.linalg.pinv(A)
    