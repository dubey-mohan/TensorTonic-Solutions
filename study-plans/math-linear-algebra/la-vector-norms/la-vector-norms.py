import numpy as np

def vector_norms(v):
    """
    Returns: float64 array of shape (3,) containing [L1, L2, L-inf] norms.
    """
    l1 = 0
    l2 = 0
    l3 = 0
    for val in v:
        l1 += abs(val)
        l2 += val ** 2
        l3 = max(abs(val), l3)

    l2 = l2 ** 0.5
    return [l1, l2, l3]
    