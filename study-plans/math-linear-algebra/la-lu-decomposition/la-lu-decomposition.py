import numpy as np

def lu_decomposition(A):
    A = np.array(A, dtype=np.float64)

    n = A.shape[0]

    L = np.eye(n, dtype=np.float64)
    U = np.zeros((n, n), dtype=np.float64)

    for i in range(n):

        # Compute U
        for j in range(i, n):
            U[i, j] = A[i, j]

            for k in range(i):
                U[i, j] -= L[i, k] * U[k, j]

        # Compute L
        for j in range(i + 1, n):
            L[j, i] = A[j, i]

            for k in range(i):
                L[j, i] -= L[j, k] * U[k, i]

            L[j, i] /= U[i, i]

    return L, U