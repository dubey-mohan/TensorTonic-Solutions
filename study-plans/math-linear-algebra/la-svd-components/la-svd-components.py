import numpy as np

def svd(A):
    A = np.array(A)
    U, s, Vt = np.linalg.svd(A, full_matrices = False)

    return U, s, Vt