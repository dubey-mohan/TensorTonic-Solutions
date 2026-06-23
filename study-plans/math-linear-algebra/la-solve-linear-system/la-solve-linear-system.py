import numpy as np

def solve_linear_system(A, b):
    A = np.array(A)
    b = np.array(b)
    return np.linalg.solve(A, b)
    