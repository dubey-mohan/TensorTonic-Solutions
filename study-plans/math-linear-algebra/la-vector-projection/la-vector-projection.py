import numpy as np

def vector_projection(u, v):
    u = np.array(u)
    v = np.array(v)
    return np.dot(np.dot(u, v) / np.dot(v, v), v)