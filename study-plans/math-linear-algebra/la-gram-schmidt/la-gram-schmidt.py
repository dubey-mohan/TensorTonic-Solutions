import numpy as np

def gram_schmidt(vectors):

    vectors = np.array(vectors, dtype=float).T
    n = vectors.shape[1]
    q = np.zeros_like(vectors, dtype=float)

    for k in range(n):
        u = vectors[:, k].copy()
        for j in range(k):
            u -= np.dot(q[:, j], vectors[:, k]) * q[:, j]

        q[:, k] = u / np.linalg.norm(u)
    return q.T