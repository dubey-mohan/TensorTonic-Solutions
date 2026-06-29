import numpy as np

def eigendecompose(A):
    val, vec = np.linalg.eig(A)
    idx = np.argsort(np.abs(val))[::-1]
    val = val[idx]
    vec = vec[:, idx]
    return (val, vec)

    
    