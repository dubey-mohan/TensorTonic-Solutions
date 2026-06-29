import numpy as np

def qr_decompose(A):
    A = np.array(A, dtype=float)

    Q, R = np.linalg.qr(A)

    # Make diagonal of R positive
    signs = np.sign(np.diag(R))
    signs[signs == 0] = 1   # avoid zeros

    D = np.diag(signs)

    Q = Q @ D
    R = D @ R

    return (Q, R)
    