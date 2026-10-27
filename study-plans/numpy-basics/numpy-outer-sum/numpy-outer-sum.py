import numpy as np

def outer_sum(a: list, b: list) -> np.ndarray:

    a = np.array(a, dtype = np.float64)
    b = np.array(b, dtype = np.float64)

    return a[:, None] + b[None, :]
