import numpy as np

def euclidean_distance(x, y):
    """
    Returns: float, the Euclidean distance between x and y.
    """
    if len(x) != len(y):
        raise ValueError("Length is not equal")
        
    n = len(x)
    s = 0
    for i in range(n):
        s += (x[i] - y[i])**2

    return s**0.5