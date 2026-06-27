import numpy as np

def low_rank_approximation(A, r):
    A = np.array(A)
    U, s, vt = np.linalg.svd(A, full_matrices = False)
    A_k = U[:, :r] @ np.diag(s[:r]) @ vt[:r, :]
    return A_k
    